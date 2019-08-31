# Import libraries
import requests
import time
from bs4 import BeautifulSoup
import json
import requests

# Set the URL you want to webscrape from
url="https://www.davidaustinroses.com/us/roses-by-type/english-roses?mode=list&limit=all"
# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
i=0
names=soup.find_all('h2','product-name')
categories=soup.find_all('div','category')
types=soup.find_all('div','type')
descriptions=soup.find_all('div','short-description')
images=soup.find_all('a','product-image')
while i<len(soup.find_all('li','clearfix item')):
    #print(soup.find_all('div','stores-weekly')[i].h3.string)
    print(names[i].text.strip())
    print(categories[i].text.strip())
    print(types[i].text.strip())
    print(descriptions[i].text.strip())
    print(names[i].a.get('href').split('/')[-1])
    print(images[i].img.get('src'))
    if descriptions[i].find_all('ul'):
        lists=descriptions[i].ul.find_all('li')
        if len(lists)>0:
            for j in range(len(lists)):
                print(lists[j].text)

    data={}
    data['image']=images[i].img.get('src')
    data['name']=names[i].text.strip()
    data['category']=categories[i].text.strip()
    data['type']=types[i].text.strip()
    data['description']=descriptions[i].text.strip()
    data['seourl']=names[i].a.get('href').split('/')[-1]
    data['lists']=[]

    if descriptions[i].find_all('ul'):
        lists=descriptions[i].ul.find_all('li')
        if len(lists)>0:
            for j in range(len(lists)):
                data['lists'].append(lists[j].text)

    print(data)
    #open('~/git/rosedata/lists/'+data['seourl']+'.json', 'a')
    with open('../rosedata/lists/'+data['seourl']+'.json', 'w+') as outfile:
        json.dump(data, outfile)

    img_data = requests.get(data['image']).content
    with open('../rosedata/images/'+data['seourl']+'.jpg', 'w+') as handler:
        handler.write(img_data)

    #print(soup.find_all('div','stores-weekly')[i].children[3])
    #for child in soup.find_all('div','stores-weekly')[i].children:
        #print(child)
    #content=BeautifulSoup(soup.find_all('div','stores-weekly'),"html.parser")

    #if content.find_all('weekly-store-special'):
        #print(content.find_all('weekly-store-special')[0])
    
    i+=1