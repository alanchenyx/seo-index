import random
import time
import urllib2
from googlesearch import search
import csv


#take a url string as input, return true if indexed by google, false otherwise
def tag_url(url):
    searchQuery = 'site:' + url
    indexed = False

    for result in search(searchQuery, tld='com.pk', lang='es', num=1, stop=1):
        time.sleep(5)
        indexed = True

    if indexed == True:
        print(url + '   ' + 'indexed')
        return indexed
    if indexed == False:
        print(url + '   ' + 'NOT indexed')
        return indexed




    # try:
    #     for result in search(searchQuery, tld='com.pk', lang='es', num=1, stop=1):
    #         time.sleep(5)
    #         resultPage.append(result)
    #
    #     if search:
    #         print(url + '   ' + 'indexed')
    #
    #     if not search:
    #         print(url + '   ' + 'NOT indexed')
    #         writeToFile.writerow([url, 'NOT indexed'])
    # except urllib2.HTTPError as err:
    #     print "Too Many Requests, waiting for 60s and retry"
    #     time.sleep(180)
    #     continue




#
# with open('result.csv', mode='w') as resultOutput:
#     writeToFile = csv.writer(resultOutput, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     writeToFile.writerow([url, 'indexed'])
#
#
#     for url in urlList:
#         searchQuery = 'site:' + url
#         resultPage = []
#
#
#         time.sleep(random.uniform(4, 7))
#




