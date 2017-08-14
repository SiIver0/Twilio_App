# Author: Noah Yoshida 
# With help from Data Science Dojo's YouTube video on webscraping in Python with BeautifulSoup
# This prorgram will return a list of parsed Yahoo Finance stories from its homepage 

def yahoo_parser():
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup 
    my_url = 'https://finance.yahoo.com'

    # OPens the connection and grabs the page 
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'html.parser')
    print(page_soup.body.span)
# Need a way to load the page further than what is normall loaded (JS 
# loads more when you scroll - you need to load this too :3 )


yahoo_parser()