import requests
import bs4
website_request=requests.get("https://www.udemy.com")
soup=bs4.BeautifulSoup(website_request.text,'lxml')
print(soup.select('title')[0].text)
for i in soup.select('.main-content'):
    print(i.text)