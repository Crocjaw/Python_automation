# Image and Video Downloader

This is a Python script that allows you to download an image or video from a URL.

## Prerequisites

1. Python 3.x
2. requests module
3. tqdm module

## Installation

`requests` and `tqdm` modules are required for the script to run. You can install them using pip:

pip install requests tqdm


## Usage

To use the script, run it using Python 3.x and pass in the URL of the image or video, the type of file to download ("mp4" or "img"), and the desired name of the downloaded file as arguments. For example:

`python downloader.py https://example.com/image.jpg img picture.jpg`


Replace `<script_name>` with the name of the script file, `<url>` with the URL of the image or video, `<type>` with either "mp4" or "img", depending on the type of file you want to download, and `<name>` with the desired name of the downloaded file.

If the file type is `mp4`, the script will download the video and display a progress bar. If the file type is `img`, the script will download the image.

## Script Details

The script first imports the necessary modules and sets up variables for the URL, file type, and file name.

There are two functions defined in the script: `img_download()` and `download_video()`. The `img_download()` function downloads an image from the given URL and saves it to the specified file name. The `download_video()` function downloads a video from the given URL, displays a progress bar during the download, and saves the video to the specified file name.

The `main()` function checks the file type and calls the appropriate download function. 

If there is an error during the download process, the script will raise an exception with an error message.

To run the script, call the `main()` function using the if statement at the bottom of the script:

if name == 'main':
main()
