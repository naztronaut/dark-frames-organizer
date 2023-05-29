# Title: Naztronomy - Dark Frames Organizer
# Author: Nazmus  Nasir + ChatGPT
# website: Naztronomy.com 
# YouTube: YouTube.com/Naztronomy 


import sys
import os
import shutil
import csv
from astropy.io import fits
from datetime import datetime

# Get the input and output directories from the command line
if len(sys.argv) < 3:
    print('Usage: python script.py input_directory output_directory [-v] [-o report_file.csv]')
    sys.exit(1)

input_directory = sys.argv[1]
output_directory = sys.argv[2]

# Check if the verbose option is provided
verbose = '-v' in sys.argv

# Get the report file name from the command line arguments
report_file = None

if '-o' in sys.argv:
    index = sys.argv.index('-o')
    if index + 1 < len(sys.argv):
        report_file = sys.argv[index + 1]

# Log file for error messages
error_log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'error.txt')

# Create the CSV report file if "-o" parameter is provided
if report_file:
    with open(report_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['File', 'Path', 'Status'])

        # Loop through each subdirectory in the input directory tree
        for subdir, _, files in os.walk(input_directory):
            # Loop through each file in the subdirectory
            for file in files:
                # Check if the file is a fits file
                if file.endswith('.fits'):
                    # Get the full path of the file
                    filepath = os.path.join(subdir, file)

                    # Open the file and read the header
                    with fits.open(filepath) as hdul:
                        header = hdul[0].header

                    # Get the header values
                    gain = header.get('GAIN', 'unknown')
                    offset = header.get('OFFSET', 'unknown')
                    temperature = header.get('CCD-TEMP', 'unknown')
                    exptime = header.get('EXPTIME', 'unknown')

                    # Format the header values
                    gain_str = f"{float(gain):.0f}" if gain != 'unknown' else 'unknown'
                    offset_str = f"{float(offset):.0f}" if offset != 'unknown' else 'unknown'
                    temperature_str = f"{float(temperature):.0f}" if temperature != 'unknown' else 'unknown'
                    exptime_str = f"{float(exptime):.0f}" if exptime != 'unknown' else 'unknown'

                    # Get the observation date from the header
                    date_obs = datetime.strptime(header['DATE-OBS'], '%Y-%m-%dT%H:%M:%S.%f').date()

                    # Create a new directory with the EXPTIME followed by " sec", temperature followed by "C", and then date
                    exptime_directory = os.path.join(output_directory, f"{exptime_str} sec")
                    temp_directory = os.path.join(exptime_directory, f"{temperature_str}C")
                    date_directory = os.path.join(temp_directory, date_obs.strftime('%Y-%m-%d'))

                    os.makedirs(date_directory, exist_ok=True)

                    # Get the file extension
                    _, extension = os.path.splitext(file)

                    # Construct the new filepath
                    counter = 1
                    new_filename = f"g{gain_str}_o{offset_str}_t{temperature_str}C_{exptime_str}sec_{counter}{extension}"
                    new_filepath = os.path.join(date_directory, new_filename)

                    # Check if the filename already exists and increment the counter until a unique filename is found
                    while os.path.exists(new_filepath):
                        counter += 1
                        new_filename = f"g{gain_str}_o{offset_str}_t{temperature_str}C_{exptime_str}sec_{counter}{extension}"
                        new_filepath = os.path.join(date_directory, new_filename)

                    # Attempt to copy the file to the new directory
                    try:
                        shutil.copy(filepath, new_filepath)
                        if report_file:
                            writer.writerow([file, new_filepath, 'Success'])
                        if verbose:
                            print(f"Successfully copied: {file}")
                    except Exception as e:
                        # Log the original filename to the error log file
                        with open(error_log_file, 'a') as err_file:
                            err_file.write(f"{file}\n")
                        if report_file:
                            writer.writerow([file, new_filepath, f'Error: {str(e)}'])
                        if verbose:
                            print(f"Failed to copy: {file}. Error: {str(e)}")
else:
    # Loop through each subdirectory in the input directory tree
    for subdir, _, files in os.walk(input_directory):
        # Loop through each file in the subdirectory
        for file in files:
            # Check if the file is a fits file
            if file.endswith('.fits'):
                # Get the full path of the file
                filepath = os.path.join(subdir, file)

                # Open the file and read the header
                with fits.open(filepath) as hdul:
                    header = hdul[0].header

                # Get the header values
                gain = header.get('GAIN', 'unknown')
                offset = header.get('OFFSET', 'unknown')
                temperature = header.get('CCD-TEMP', 'unknown')
                exptime = header.get('EXPTIME', 'unknown')

                # Format the header values
                gain_str = f"{float(gain):.0f}" if gain != 'unknown' else 'unknown'
                offset_str = f"{float(offset):.0f}" if offset != 'unknown' else 'unknown'
                temperature_str = f"{float(temperature):.0f}" if temperature != 'unknown' else 'unknown'
                exptime_str = f"{float(exptime):.0f}" if exptime != 'unknown' else 'unknown'

                # Get the observation date from the header
                date_obs = datetime.strptime(header['DATE-OBS'], '%Y-%m-%dT%H:%M:%S.%f').date()

                # Create a new directory with the EXPTIME followed by " sec", temperature followed by "C", and then date
                exptime_directory = os.path.join(output_directory, f"{exptime_str} sec")
                temp_directory = os.path.join(exptime_directory, f"{temperature_str}C")
                date_directory = os.path.join(temp_directory, date_obs.strftime('%Y-%m-%d'))

                os.makedirs(date_directory, exist_ok=True)

                # Get the file extension
                _, extension = os.path.splitext(file)

                # Construct the new filepath
                counter = 1
                new_filename = f"g{gain_str}_o{offset_str}_t{temperature_str}C_{exptime_str}sec_{counter}{extension}"
                new_filepath = os.path.join(date_directory, new_filename)

                # Check if the filename already exists and increment the counter until a unique filename is found
                while os.path.exists(new_filepath):
                    counter += 1
                    new_filename = f"g{gain_str}_o{offset_str}_t{temperature_str}C_{exptime_str}sec_{counter}{extension}"
                    new_filepath = os.path.join(date_directory, new_filename)

                # Attempt to copy the file to the new directory
                try:
                    shutil.copy(filepath, new_filepath)
                    if verbose:
                        print(f"Successfully copied: {file}")
                except Exception as e:
                    # Log the original filename to the error log file
                    with open(error_log_file, 'a') as err_file:
                        err_file.write(f"{file}\n")
                    if verbose:
                        print(f"Failed to copy: {file}. Error: {str(e)}")
