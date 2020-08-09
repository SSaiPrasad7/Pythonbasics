import bs4
import requests
base_url="http://books.toscrape.com/catalogue/page-{}.html"

three_star_title=[]
for n in range(1,51):
    scrape_url=requests.get(base_url.format(n))
    soup=bs4.BeautifulSoup(scrape_url.text,'lxml')
    books=soup.select('.product_pod')
    for book in books:
        if len(book.select('.star-rating.Three'))==0:
            book_title=book.select('a')[1]['title']
            three_star_title.append(book_title)
print(three_star_title)
