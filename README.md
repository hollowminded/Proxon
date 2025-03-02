# PROXON - Proxy Scraper and Checker

## Overview
PROXON is a powerful tool for scraping and validating HTTP and HTTPS proxies. It fetches proxies from multiple sources, checks their validity, and categorizes them based on protocol type.

## Features
- **Scraper**: Fetches proxies from various sources online.
- **Checker**: Validate proxies.
- **Multithreading**: Uses concurrent threads for faster proxy checking.
- **Color-coded Output**: Enhanced visibility with colored terminal output.

## Requirements
Make sure you run install.bat, or install the following dependencies before using the script:

```sh
pip install requests bs4 colorama
```

## Usage
Run the script and select an option from the main menu:

```sh
python proxon.py
```

### Main Menu
```
[1] Scraper - Fetches proxies from multiple sources.
[2] HTTP/S Checker - Validates and categorizes proxies.
[3] SOCKS5 Checker - (Work in Progress)
[0] FAQ - Information about the tool.
```

### Scraper
- Gathers proxies from various online sources.
- Saves them in `proxies.txt`.

### Checker
- Reads `proxies.txt`.
- Validates proxies by making requests.
- Saves working proxies to `proxies/http_proxies_<timestamp>.txt` and `proxies/https_proxies_<timestamp>.txt`.

## Notes
- SOCKS5 checking is currently a work in progress.
- Invalid proxies will be ignored.

## To-Do
- Improve proxy checking algorithm.
- Add SOCKS5 support.
- Enhance user interface.

## Disclaimer
This tool is intended for educational and research purposes only. The developer is not responsible for any misuse.

