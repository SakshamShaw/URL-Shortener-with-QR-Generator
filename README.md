# URL-Shortener-with-QR-Generator

## Description
This Python project takes a URL, shortens it using the TinyURL service, and generates a QR code for the shortened URL. The QR code is displayed to the user instead of being saved as a file.

## Features
- Shortens URLs using `pyshorteners` (TinyURL API)
- Generates and displays a QR code for the shortened URL
- Simple and user-friendly command-line interface

## Installation

Ensure you have Python installed, then install the required dependencies:
```bash
pip install pyshorteners qrcode[pil] matplotlib
```

## Usage

Run the script and enter the URL you want to shorten:
```bash
python url_shortener_qr.py
```

Follow the prompts:
1. Enter the original URL.
2. The script will return a shortened URL.
3. A QR code will be displayed for easy sharing.

## Example
```
Enter the URL to shorten:[ https://example.com](https://www3.ecommercestore.com/?tm=1&subid4=1739046280.0102350000&KW1=Best%20Mortgage%20Refinancing%20Rates&KW2=Elite%20Dating%20Services&KW3=Dedicated%20Gaming%20Servers&KW4=Online%20Career%20Counseling%20Programs&KW5=Make%20Money%20From%20Home&KW6=Make%20Money%20From%20Home&KW7=Elite%20Dating%20Service&KW8=Elite%20Dating%20Service&KW9=Free%20Credit%20Card%20Apply&searchbox=0&backfill=0)
Shortened URL:  https://tinyurl.com/2anqkcu3
[QR Code is displayed]
```

## License
This project is open-source and available under the MIT License.

## Contributions
Feel free to contribute by submitting issues or pull requests!

## Author
Saksham Shaw

