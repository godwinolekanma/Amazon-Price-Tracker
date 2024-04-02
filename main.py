import os
import requests
from bs4 import BeautifulSoup
import smtplib

# Constants
AMAZON_ITEM_URL = "https://www.amazon.com/LG-UltraGear-3840x2160-DisplayHDR-DisplayPort/dp/B0C63B9CZX/ref=sr_1_5?crid=2S175GWVOAYXY&dib=eyJ2IjoiMSJ9.ugrqgk2TsP0IWxnGesCzthSyJAgrtbR-_Z3xUezfGLmEr4SAFhR-aHCSnHsgHTNc61_CgGPMAc6PR6edZZ1l1lgR2sz-izudqLDSzTvCA9Y290TGDI_HybeOUNOunZYvIdly83HbT1dCsQdd9M0rpvDkLOB3T_7Oo6SZzhRiERgDrPv-4-4SRuQhLkRJfLL2eRueD3b6DSzZTzWuxWG4Gxe8nLcBboLfBcffHmuj5cI.ACsrO9x4DY38xu5SmTnmRSG6C7zlLniKVJS_F9fsgb4&dib_tag=se&keywords=4k%2Bmonitor%2Blg&qid=1709400873&sprefix=4k%2Bmonitor%2Blg%2Caps%2C106&sr=8-5&th=1"
AGENT = os.environ.get('AGENT')
ACC_LANG = "en-US,en;q=0.9"
BUY_PRICE = 600
MY_MAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

# Set up request headers
header = {
    "User-Agent": AGENT,
    "Accept-Language": ACC_LANG
}

# Send request to Amazon to get product information
response = requests.get(url=AMAZON_ITEM_URL, headers=header)
amazon_website = response.text

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(amazon_website, "html.parser")

# Extract current price and product title from Amazon page
current_price = int(str(soup.find(name="span", class_="a-price-whole").getText()).split(".")[0])
product_title = str(soup.find(name="span", id="productTitle").getText()).lstrip()

# Check if the current price is below the desired buy price
if current_price < BUY_PRICE:
    # Establish connection to Gmail SMTP server
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    # Login to Gmail account
    connection.login(user=MY_MAIL, password=PASSWORD)
    # Send email alert with product information
    connection.sendmail(
        from_addr=MY_MAIL,
        to_addrs=MY_MAIL,
        msg=f"Subject:Amazon Price Alert\n\n{product_title}\nnow ${current_price}\n{AMAZON_ITEM_URL}"
    )