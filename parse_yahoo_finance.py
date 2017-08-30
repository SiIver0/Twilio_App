#!/usr/bin/env python

__author__          = 'Noah Yoshida' 
__email__           = 'nyoshida@nd.edu'

'''
With help from https://www.youtube.com/watch?v=XQgXKtPSzUI
This prorgram will return a list of parsed Yahoo Finance stories from its homepage.
'''
# Doesn't really work.. the yahoo rss page has weird formatting 

def yahoo_parser():
    import feedparser
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup 
    from datetime import datetime
    import re

    # Popular Stories
    # my_url = 'https://finance.yahoo.com/rss/popularstories'
    my_url = 'https://rss.cnn.com/rss/money_technology.rss'
    f = feedparser.parse(my_url)
    print(str(f.feed.title))


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
        d = item.description.text
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr,'',d)
        print(cleantext)
        descrpitions.append(cleantext)
        dates.append(str(item.pubDate.text))

    return [titles,descrpitions,dates]


x = yahoo_parser()

# for i in range(len(x[0])):
#     print('-------------')
#     print(x[0][i])
#     print(x[1][i])
#     print(x[2][i])