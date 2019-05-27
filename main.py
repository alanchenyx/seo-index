import sitemap
import indextagger
def main():
    print('welcome')

    # get url list from xml sitemap
    # sitemaplink = raw_input('Enter your sitemap link to start~ \n')

    sitemaplink = 'https://thethreeseas.com.au/post-sitemap.xml'


    urlList = sitemap.get_url_list(sitemaplink)

    # urlList = ['https://thethreeseas.com.au/schoolies/', 'https://www.gawertfwefawefasdfaedasfaswfe.com/',
    #            'https://thethreeseas.com.au/universalchildrensday/', 'https://thethreeseas.com.au/news-test/']

    for url in urlList:
        indextagger.tag_url(url)




if __name__ == "__main__":
    main()

