# PDF Table Extractor

PDF Table Extractor is a Python script that allows you to extract tables from a PDF file and export them in the format of your choice. The script uses the camelot library to read the specified pages of the PDF and extract tables from them.

## Features

- Extract tables from a PDF file.
- Specify the pages and ranges you want to extract tables from.
- Export the extracted tables in the format of your choice: 'json', 'excel', 'html', 'markdown', or 'sqlite'.
- Easy-to-use command-line interface.

## Installation

1. Clone the repository: 

`git clone https://github.com/username/pdf-table-extractor.git`


2. Install the dependencies:

pip install camelot-py[cv]


## Usage

1. Navigate to the project directory:

cd pdf-table-extractor


2. Run the script:

`python pdf_table_extractor.py path/to/file.pdf 1,2-10,... format output_name`


- `path/to/file.pdf`: replace with the path to the PDF file you want to extract tables from.
- `1,2-10,...`: specify the pages and ranges you want to extract tables from.
- `format`: specify the output format you want to export the tables in. Available options are: 'json', 'excel', 'html', 'markdown', or 'sqlite'.
- `output_name`: specify the name of the output file.

3. The extracted tables will be saved in the specified output format and file name.

