# Web_Code_Generator

This is a simple web scraping script that extracts blog post titles and links from a specified website using Python's `requests` and `BeautifulSoup` libraries.

## Features

- Sends a GET request to the specified website.
- Parses the HTML content of the page.
- Extracts and prints the titles and links of blog posts.
- Handles HTTP request errors and checks for the presence of blog posts.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository or download the script.
2. Install the required libraries using `pip`:

    ```bash
    pip install requests beautifulsoup4
    ```

## Usage

1. Run the script and enter the URL of the website you want to scrape when prompted:

    ```bash
    python scraper.py
    ```

2. The script will send a GET request to the specified URL, parse the HTML content, and print the titles and links of the blog posts found on the page.

## Example

```bash
Enter the URL of the website to scrape: https://example.com/blog
