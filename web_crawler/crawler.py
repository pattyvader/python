import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/blogs/"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

#nicely formatted string
print (soup.prettify())

#obtains all attributtes 'href'
for links in soup.find_all('a', href=True):
    print links['href']
