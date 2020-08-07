import requests
import bs4
website_request1=requests.get("https://en.wikipedia.org/wiki/Mark_Zuckerberg")
soup=bs4.BeautifulSoup(website_request1.text,'lxml')
image_link=soup.select('.image')[0]
print(image_link)
image_request=requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Mark_Zuckerberg_F8_2019_Keynote_%2832830578717%29_%28cropped%29.jpg/220px-Mark_Zuckerberg_F8_2019_Keynote_%2832830578717%29_%28cropped%29.jpg")
f=open('markzuckerberg.jpg','wb')
f.write(image_request.content)
f.close()