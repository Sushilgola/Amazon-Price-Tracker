import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.amazon.in"
URL = "https://www.amazon.in/dp/B08XQ89VFP"

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

base_response = requests.get(BASE_URL, headers=headers)
cookies = base_response.cookies

response = requests.get(URL, cookies=cookies)

soup = BeautifulSoup(response.content, 'html.parser')

price_lst = soup.find_all(class_="aok-offscreen")
print(price_lst)

