# Amazon Price Tracker

This Python script allows you to track the price of a product on Amazon and receive email alerts when the price drops below a specified threshold.

## How It Works

1. The script sends a GET request to the Amazon product page using the provided URL.
2. It parses the HTML content of the page using BeautifulSoup to extract the current price and product title.
3. If the current price is lower than the specified threshold, the script sends an email alert using SMTP.

## Prerequisites

- Python 3.x
- `requests` library: `pip install requests`
- `beautifulsoup4` library: `pip install beautifulsoup4`
- An Amazon account and a Gmail account (for sending email alerts)

## How to Use

1. Clone this repository:

        git clone https://github.com/godwinolekanma/Amazon-Price-Tracker.git
2. Install dependencies

        pip install -r requirements.txt
3. Modify the script with your Amazon product URL

4. Run the program

## Configuration
- AMAZON_ITEM_URL: URL of the Amazon product page.
- AGENT: User-agent string for the HTTP request (get this at http://myhttpheader.com/).
- BUY_PRICE: Desired buy price for the product.
- MY_MAIL: Your Gmail email address.
- PASSWORD: Your Gmail account password (you may need to enable "less secure apps" in your Gmail settings).

## Note 
- use pythonanywhere to run this code everyday https://www.pythonanywhere.com/