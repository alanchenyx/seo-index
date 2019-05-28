import csv
import datetime
import sitemap
import indextagger
def main():
    print('welcome, starting at '+str(datetime.datetime.now()))

    # get url list from xml sitemap
    # sitemaplink = raw_input('Enter your sitemap link to start~ \n')

    sitemaplink = 'https://thethreeseas.com.au/post-sitemap.xml'


    urlList = sitemap.get_url_list(sitemaplink)

    # urlList = ['https://thethreeseas.com.au/schoolies/', 'https://www.gawertfwefawefasdfaedasfaswfe.com/',
    #            'https://thethreeseas.com.au/universalchildrensday/', 'https://thethreeseas.com.au/news-test/']


    with open('result.csv', mode='w') as resultOutput:
        writeToFile = csv.writer(resultOutput, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in urlList:
            if indextagger.tag_url(url):
                print(url + '   ' + 'indexed')
                writeToFile.writerow([url, 'indexed'])
                resultOutput.flush()
            if not indextagger.tag_url(url):
                print(url + '   ' + 'NOT indexed')
                writeToFile.writerow([url, 'NOT indexed'])
                resultOutput.flush()

    print('all done, finished at ' +str(datetime.datetime.now()))

    urlList = ['thethreeseas.com.au']

    indextagger.tag_url('thethreeseas.com.au')

    print('all done, finished at ' +str(datetime.datetime.now()))


if __name__ == "__main__":
    main()

