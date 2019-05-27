#this class handles site map link
#takes in a xml sitemap link and outputs a list of urls

import requests
from bs4 import BeautifulSoup
import re

def make_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup


# put urls in a list
def get_xml_urls(soup):
    urls = [loc.string for loc in soup.find_all('loc')]
    return urls


# get the img urls
def get_src_contain_str(soup, string):
    srcs = [img['src'] for img in soup.find_all('img', src=re.compile(string))]
    return srcs

def get_url_list(sitemaplink):
    xml = sitemaplink
    soup = make_soup(xml)
    urls = get_xml_urls(soup)
    return urls