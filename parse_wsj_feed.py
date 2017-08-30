#!/usr/bin/env python

__author__          = 'Noah Yoshida' 
__email__           = 'nyoshida@nd.edu'

'''
With help from https://www.youtube.com/watch?v=XQgXKtPSzUI
This prorgram will return a list of parsed WSJ market stories from its homepage, taking advantage of WSJ's RSS xml file feed.

It grabs the titles, descriptions, and the dates of the news items as strings and outputs them as a list. 
'''

def wsj_parser():
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup 
    from datetime import datetime
    # World News 
    # my_url = 'https://www.wsj.com/xml/rss/3_7031.xml' 
    # Technology : What's New 
    # my_url = 'https://www.wsj.com/xml/rss/3_7455.xml'
    # Opinion
    # my_url = 'https://www.wsj.com/xml/rss/3_7041.xml'
    # U.S. Business
    # my_url = 'https://www.wsj.com/xml/rss/3_7014.xml'
    # World News 
    my_url = 'https://www.wsj.com/xml/rss/3_7085.xml'

    # Opens the connection and grabs the page 
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'xml')

    titles = []
    descrpitions = []
    dates = []

    for item in page_soup.findAll('item'):
        titles.append(item.title.text)
        descrpitions.append(item.description.text)
        dates.append(str(item.pubDate.text))

    return [titles,descrpitions,dates]

# ========= Testing ==========
x = wsj_parser()

for i in range(len(x[0])):
    print('-------------')
    print(x[0][i])
    print(x[1][i])
    print(x[2][i])
