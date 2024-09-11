# Web Scraper

This is a simple web scraper that allows you to search for information on a given topic and scrape the text from the top results from a specified domain.

## Features

- Searches for information using DuckDuckGo search engine
- Scrapes text from the top results from a specified domain
- Uses NLTK's sentence tokenizer to split the scraped text into sentences
- Cleans the scraped text by removing non-alphanumeric characters

## Requirements

- Python 3.x
- DuckDuckGo search API (`duckduckgo_search` package)
- Requests library (`requests` package)
- BeautifulSoup 4 (`beautifulsoup4` package)
- NLTK (`nltk` package)

## Installation

1. Clone the repository:
```
git clone https://github.com/Singhchandann/Web-Scraper.git
```
2. Install the required packages:
```
pip install duckduckgo_search requests beautifulsoup4 nltk
```
3. Download the NLTK sentence tokenizer data:
```
python
>>> import nltk
>>> nltk.download("punkt")
```

## Usage

1. Run the `scraper.py` script:
```
python scraper.py
```
2. Enter your search query:
```
Enter Your query: example query
```
3. Enter the domain you want to scrape from:
```
Enter the domain you want to scrape from (e.g., wikipedia.com, reddit.com): example.com
```
4. The script will print the URLs of the top results and the scraped text from each URL.

## Note

The `duckduckgo_search` package is not officially supported by DuckDuckGo and may violate their terms of service. Use at your own risk.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
