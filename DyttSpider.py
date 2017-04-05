#coding=utf-8

import urllib
import urllib2
import chardet
import threading
import re
import time
import MySQLdb
from lxml import etree
from bs4 import BeautifulSoup

for num in range(1,6):
    url = "http://www.ygdy8.net/html/gndy/dyzz/list_23_" + str(num) + ".html"
    #print url
    #response = urllib2.urlopen('http://www.ygdy8.net/html/gndy/dyzz/index.html')
    response = urllib2.urlopen(url)
    html = response.read()
    #html = html.decode('unicode').encode('gb2312')
    #soup = BeautifulSoup(html)
    #print soup.prettify()
    #html = html.decode('gbk','ignore').encode('utf-8')
    html = html.decode('gbk','ignore')
    tree=etree.HTML(html)
    #tree=etree.HTML(html.lower().decode('gbk'))
    ulink = tree.xpath(u"//a[@class='ulink']")
    g_pages=[]
    for n in ulink:
        g_pages.append("http://www.ygdy8.net" + str(n.attrib['href']))
        #print n.attrib['href']
        #i=i+1
    for i in g_pages:
        m_response = urllib2.urlopen(i)
        m_html = m_response.read()
        m_html = m_html.decode('gbk','ignore')
        #print m_html
        m_tree=etree.HTML(m_html)
        moviename = m_tree.xpath(u"//title")
        #soup = BeautifulSoup(html)
        #print tree
        movieurl = m_tree.xpath(u"//tbody/tr/td/a")
        #print len(movieurl)
        #IMDb = re.findall("(...)/10 from",m_html,re.S)
        IMDb = re.findall("(...)/10 from",m_html,re.S)
        db = MySQLdb.connect("localhost","root","123","bigdata",charset = 'utf8' )
                #db = MySQLdb.connect("localhost","root","123","bigdata",charset = 'utf8' )
                # 使用cursor()方法获取操作游标
        cursor = db.cursor()
                #m[0].decode('utf-8').encode('gb2312')
        if len(IMDb)>0:
            sql="insert into dytt values('%s','%s','%s','%s')"%(moviename[0].text,i,movieurl[0].text,IMDb[0])
        else:
            sql="insert into dytt values('%s','%s','%s','%s')"%(moviename[0].text,i,movieurl[0].text,'')
        cursor.execute(sql)
        db.commit()
        #if len(IMDb)>0:
        #    print IMDb[0]
        '''
        s_moviename=""
        s_movieurl=""
        for m in moviename:
        #    print m.text
            s_moviename = m.text
        for s in movieurl:
        #    print s.text
            s_movieurl = s.text
        '''
    #print html
 # 打开数据库连接
        '''
        for m in moviename:
            for s in movieurl:
                db = MySQLdb.connect("localhost","root","123","bigdata",charset = 'utf8' )
                #db = MySQLdb.connect("localhost","root","123","bigdata",charset = 'utf8' )
                # 使用cursor()方法获取操作游标
                cursor = db.cursor()
                #m[0].decode('utf-8').encode('gb2312')
                if len(IMDb)>0:
                    sql="insert into dytt values('%s','%s','%s','%s')"%(m.text,i,s.text,IMDb[0])
                else:
                   sql="insert into dytt values('%s','%s','%s','%s')"%(m.text,i,s.text,"null")
                cursor.execute(sql)
                db.commit()

             #   print m[0]+html
        db.close()
        cursor.close()
        '''