import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import json
from datetime import datetime



def yahoo(item):
    print('=== yahoo ===',item)

    # yahoo
    url = f'https://tw.buy.yahoo.com/search/product?p={item}'
    r = requests.get(url)
    response = r.text
    soup = BeautifulSoup(response,'html.parser')

    ## 找出連結
    reg = re.compile('sc-jOFryr')
    items = soup.find_all('a',class_=reg)
    links =[item['href'] for item in items]

    products=[]

    for link in links:
        r=requests.get(link)
        soup = BeautifulSoup(r.text,'html.parser')
        # 字典把同商品放一起
        product = {}
        product['link'] = link
        product['name'] = soup.find('h1',class_='HeroInfo__title___57Yfg HeroInfo__textTooLong___BXk8j').text
        product['price'] = soup.find('div',class_='HeroInfo__mainPrice___1xP9H').text
        products.append(product)
    df_yahoo=pd.DataFrame(products)
    df_yahoo['source'] = "Yahoo"
    df_yahoo['time']=datetime.today()
    return df_yahoo

def momo(item):
    print('=== momo ===',item)
    header = {
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    url = f'https://m.momoshop.com.tw/search.momo?searchKeyword={item}&searchType=1&cateLevel=-1&ent=k&_imgSH=fourCardStyle'
    r = requests.get(url,headers=header)
    soup = BeautifulSoup(r.text,'html.parser')
    items = soup.find('article',class_='prdListArea').find_all('li')
    links = [ item.a['href'] for item in items ]


    products=[]
    for link in links:
        link = 'https://www.momoshop.com.tw/goods/GoodsDetail.jsp?' + (link.split('?')[1])
        r = requests.get(link,headers=header)
        soup = BeautifulSoup(r.text,'html.parser')
        product={}
        product["name"] = soup.find('span',id='osmGoodsName').text
        product['link']= link
        product['price']= soup.find('li',class_='special').text
        products.append(product)

    df_momo = pd.DataFrame(products)
    df_momo['source'] = "momo"
    df_momo['time']=datetime.today()
    return df_momo

def pchome(item):
    print('=== pchome ===',item)
    url = f'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={item}&page=1&sort=sale/dc'
    r = requests.get(url)
    response = json.loads(r.text)

    products = [
        {
            'name': d['name'],
            'price': d['price'],
            'link': 'https://24h.pchome.com.tw/prod/' + d['Id']
        } for d in response['prods']
    ]

    df_pc = pd.DataFrame(products)
    df_pc['source'] = 'Pchome'
    df_pc['time'] = datetime.today()
    return df_pc

