import requests
from bs4 import BeautifulSoup

URL = 'https://www.newegg.com/asus-90lm01h1-b013b0-21-5-full-hd/p/N82E16824236974'


headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id = "grpDescrip_24-236-974").get_text()
price = soup.find(id = "strong")
#converted_price = price[0:5]

print(title)
print(price)

