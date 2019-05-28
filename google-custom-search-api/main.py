from googleapiclient.discovery import build
import sitemap


def main():
    #getlist of urls from sitemap
    sitemaplink = 'https://thethreeseas.com.au/post-sitemap.xml'
    sitemapUrls = sitemap.get_url_list(sitemaplink)
    try:
        for siteUrl in sitemapUrls:
            query = 'site:' + siteUrl
            index = False
            # Build a service object for interacting with the API. Visit
            service = build("customsearch", "v1", developerKey="AIzaSyAph8h_x_ykE7SzM2SdOQvdfJuVoX0oukc")

            res = service.cse().siterestrict().list(
                q=query,
                cx='016954827200140921014:rlov2hdoca0', ).execute()

            # print(res)
            for item in res['items']:
                url = item['formattedUrl'].replace(" ", "")
                if url == siteUrl:
                    index = True

            if index:
                print(siteUrl + '  indexed')
            if not index:
                print(siteUrl + '  not indexed')
    except KeyError:
        #this means no result return, therefore not indexed
        print(siteUrl + '  not indexed')



if __name__ == '__main__':
    main()