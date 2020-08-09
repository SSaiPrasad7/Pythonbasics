import requests
import bs4
website_request1=requests.get("https://en.wikipedia.org/wiki/Mark_Zuckerberg")
soup=bs4.BeautifulSoup(website_request1.text,'lxml')
image=soup.select('.image')[0]
image_link=image.select('img')[0]['src']
image_request=requests.get(f"https:{image_link}")
f=open('markzuckerberg.jpg','wb')
f.write(image_request.content)
f.close()