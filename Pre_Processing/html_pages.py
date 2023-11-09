import os
import urllib.request
import re


def htmlPagesCrawl():
            heads = {'headers':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'}

            if not os.path.exists('newDocs'):
                os.makedirs('newDocs')

            file1 = open("web_crawler/crawled.txt","r")
            urlsList = file1.readlines()

            for i in range(1,len(urlsList)+1):
                try:
                    seedUrl = urlsList[i].strip()
                    n = requests.get(seed_url, headers=heads)
                    al = n.text
                    fileTitle = al[al.find('<title>') + 7 : al.find('</title>')]
                    fileTitle = re.sub('[^A-Za-z0-9]+', '', fileTitle)
                    print(fileTitle)

                    # Identify ourselves to be polite.
                    request = urllib.request.Request(seed_url)
                    request.add_header("Mohammed Abdul", "Mini Search Engine Project")
                    opener = urllib.request.build_opener()
                    response = opener.open(request)
                    html = response.read()

                    # Save the content to files that are named after the URL.
                    f = open('newDocs/{}.txt'.format(fileTitle), 'w+')
                    f.write(seed_url+"\n"+str(html))
                    f.write(html)
                    f.close()
                except:
                    print("Page Error")


if __name__ == "__main__":
    htmlPagesCrawl()


