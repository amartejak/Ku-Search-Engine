from urllib.request import urlopen
from link_finder import LinkFinder
from domain import *
from general import *
#import main


class WebSpider:

    Project_Name = ''
    baseUrl = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, Project_Name, baseUrl, domain_name):
        WebSpider.Project_Name = Project_Name
        WebSpider.baseUrl = baseUrl
        WebSpider.domain_name = domain_name
        WebSpider.queue_file = WebSpider.Project_Name + '/queue.txt'
        WebSpider.crawled_file = WebSpider.Project_Name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider', WebSpider.baseUrl)

    # Creates directory and files for project on first run and starts the spider
    @staticmethod
    def boot():
        create_project_dir(WebSpider.Project_Name)
        createDataFiles(WebSpider.Project_Name, WebSpider.baseUrl)
        WebSpider.queue = fileToSet(WebSpider.queue_file)
        WebSpider.crawled = fileToSet(WebSpider.crawled_file)

    # Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(thread_name, pageUrl):
       
         if pageUrl not in WebSpider.crawled:
            print(thread_name + ' now crawling ' + pageUrl)
            print('Queue ' + str(len(WebSpider.queue)) + ' | Crawled  ' + str(len(WebSpider.crawled)))
            WebSpider.add_links_to_queue(WebSpider.gather_links(pageUrl))
            WebSpider.queue.remove(pageUrl)
            WebSpider.crawled.add(pageUrl)
            WebSpider.update_files()


    # Converts raw response data into readable information and checks for proper html formatting
    @staticmethod
    def gather_links(pageUrl):
        html_string = ''
        try:
            response = urlopen(pageUrl)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(WebSpider.baseUrl, pageUrl)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    # Saves queue data to project files
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in WebSpider.queue) or (url in WebSpider.crawled):
                continue
            if WebSpider.domain_name != get_domain_name(url):
                continue
            WebSpider.queue.add(url)

    @staticmethod
    def update_files():
        setToFile(WebSpider.queue, WebSpider.queue_file)
        setToFile(WebSpider.crawled, WebSpider.crawled_file)
