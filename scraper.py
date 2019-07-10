import requests
import smtplib
from bs4 import BeautifulSoup

URL = 'https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07NLTXWZT/ref=sr_1_3?th=1'


headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    converted_price = float(price[3:9])

    #if(converted_price < 3.910)
    send_mail()

    print(title.strip())
    print(converted_price)

def send_mail():
    #add the server number thingy 
    server = smtplib.SMTP('smtp.gmail.com',)
    server.ehlo()
    server.starttls
    server.elho()
    server.login()

