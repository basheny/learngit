#/bin/python3.6
#-*-coding:utf-8-*-

import requests
from bs4 import BeautifulSoup

def getUrl():    #获得豆瓣10页的url地址
    for i in range(0, 250, 25):
        url = 'https://book.douban.com/top250?start=' + str(i)
        yield url
    
def getBook(url):    #将得到的url进行解析
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    book_tag = soup.find_all('table', {'width': '100%'})
    for item in book_tag:
        b = item.find('a')
        print('书   名：' +  ' '+item.find('div').find('a')['title'])    #打印爬取到的信息
        print('出版信息：' +  item.find('p').get_text())
        print('豆瓣地址：' , b['href'])
        print('封   面：' , b.find('img')['src'])
        print('\n')

for url in getUrl():
    getBook(url)

