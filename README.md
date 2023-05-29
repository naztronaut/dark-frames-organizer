# Naztronomy - Dark Frames Organizer

This script is designed to process FITS files, read their header information, and organize them into a structured directory hierarchy based on their header attributes. It also provides options for verbose output and generating a CSV report of the file processing results.

## Dependencies

This script requires the following dependencies:

- Python (version 3.x)
- astropy library

## Installation

To install the necessary dependencies, follow these steps:

1.  Install Python 3.x: Visit the official Python website at [python.org](https://www.python.org) and download the latest version of Python for your operating system. Follow the installation instructions provided.
2.  Install the astropy library: Open a terminal or command prompt and run the following command:

    pip install astropy

This will install the astropy library required by the script.

## Usage

    python dfo.py input_directory output_directory [-v] [-o report_file.csv]

### Arguments

- `input_directory`: The directory where the script looks for the FITS files to process.
- `output_directory`: The directory where the processed files will be organized into the new directory structure.
- `-v` (optional): Enables verbose output. Success and failure messages will be displayed during the file processing.
- `-o report_file.csv` (optional): Specifies the filename of the CSV report file. If not provided, the default filename "report.csv" will be used.

## Functionality

The script performs the following tasks:

1.  Reads the FITS files' header information including gain, offset, temperature, and exposure time.
2.  Creates a new directory structure based on the header attributes in the output directory.

        The directory structure follows the format:

        output_directory/EXPTIME/temperature/YYYY-MM-DD/
        
        Where:
        
        - `EXPTIME`: The exposure time of the FITS file.
        - `temperature`: The rounded CCD temperature of the FITS file, divisible by 5.
        - `YYYY-MM-DD`: The date of the FITS file.
        
        Example directory names:
        
        - 60sec/-10C/2023-05-01/
        - 120sec/5C/2023-05-02/

3.  Renames the files according to the header attributes and moves them to the corresponding directories.
4.  Optionally generates a CSV report file with the file processing results.

## Example Usage

To process FITS files located in the `input_files` directory and organize them into the `output_files` directory with verbose output and report file:

    python dfo.py input_files output_files -v -o report.csv

This command will process the FITS files, display success and failure messages during the process, and generate a CSV report file named `report.csv` containing the processing results.



## Authors
* **Nazmus Nasir** - [Nazmus](https://nazm.us) of [https://www.naztronomy.com](Naztronomy.com)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Questions ?
Have questions? You can reach me through several different channels. You can ask a question in the  [issues forum](/../../issues) or on the video comments on [https://www.youtube.com/naztronomy](YouTube). 


## Contribute 
I will accept Pull requests fixing bugs or adding new features after I've vetted them. Feel free to create pull requests!  
