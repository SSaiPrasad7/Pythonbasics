import requests
import bs4
base_url='http://quotes.toscrape.com/page/{}/'
website_request=requests.get(base_url.format(1))
soup=bs4.BeautifulSoup(website_request.text,'lxml')
author=soup.select('.author')
author_list=[]
quote_list=[]
for i in range(len(author)):
    author_list.append(author[i].text)
print(set(author_list))
quotes=soup.select('.text')
for i in range(len(quotes)):
    quote_list.append(quotes[i].text)
print(quote_list)
tags=soup.select('.tag-item')
for i in range(len(tags)):
    print(tags[i].text)

page_still_valid = True
authors = set()
page = 1
url='http://quotes.toscrape.com/page/'
while page_still_valid:
    page_url = url + str(page)+'/'
    res = requests.get(page_url)
    if "No quotes found!" in res.text:
        break
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    for name in soup.select(".author"):
        authors.add(name.text)
    page += 1
print(authors)