import csv
import time
from googlesearch import search


#take a url string as input, return true if indexed by google, false otherwise
from retrying import retry


@retry(wait_random_min=600000, wait_random_max=800000)
def tag_url(url):
    searchQuery = 'site:' + url
    indexed = False

    for result in search(searchQuery, tld='com.pk', lang='es', num=1, stop=1):
        time.sleep(2)
        indexed = True

    if indexed == True:
        return indexed
    if indexed == False:
        return indexed

