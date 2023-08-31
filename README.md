# ITB-PDF_Excel-DataScraper
Welcome to the ITB PDF Data Scraper project. This script allows you to extract and organize information from PDF files obtained from the ITB Berlin website.

**Important Note:** 
While developing this project, there were no restrictions in scraping the ITB website. However, before running the scripts, we strongly recommend that you read and understand the `robots.txt` file of the website you intend to scrape. Make sure to respect any guidelines or restrictions mentioned in that file.

## Overview

The ITB PDF Data Scraper is a Python script designed to extract key information from PDF files available on the ITB Berlin website. The script uses libraries such as PyPDF2, openpyxl, and requests to perform the following tasks:

- Scans a directory for PDF files related to ITB exhibitors.
- Extracts relevant data like organization details, contact information, and social media links from each PDF.
- Organizes the extracted data into an Excel spreadsheet for easy analysis.

## Usage

1. Clone this repository to your local machine.
2. **Scrape and Load Data:**
   - Run the script `Organizer_Data_Scraper.py` using Python.
   - This script scrapes ITB exhibitor data and creates `organizations_data.csv` containing organization IDs and names.

3. **Generate PDF URLs:**
   - Execute the script `URL_Generator.py` using Python.
   - This script reads the `organizations_data.csv` and generates valid URLs, saving them to `PDF_URLs_5567.txt`.

4. **Download PDF Files:**
   - Launch the script `PDF_Downloader.py` to start downloading PDF files.
   - The URLs from `PDF_URLs_5567.txt` are used to fetch and store the PDFs in a designated folder.

5. **Extract Data from PDFs:**
   - Run the script `Data_Extractor.py` using Python.
   - This script extracts detailed information from each downloaded PDF and compiles it into an Excel file named `Results-openpyxl.xlsx`.

## Installation

1. Clone the repository: `git clone https://github.com/Siva-DataSearch/ITB_PDF_DataScraper.git`
2. Install required packages: `pip install -r requirements.txt`

## Dependencies

- PyPDF2
- openpyxl
- requests

## Credits

Developed by [Siva](https://github.com/Siva-DataSearch)
