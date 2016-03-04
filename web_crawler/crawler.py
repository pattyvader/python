import requests
from bs4 import BeautifulSoup

url = "https://pt.wikipedia.org/wiki/Python"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

for links in soup.find_all('a', href=True):
    print links['href']
