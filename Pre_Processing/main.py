import threading
from queue import Queue
from spider import WebSpider
from domain import *
from general import *

Project_Name = 'web_crawler'
HomePage =  'https://ku.edu'
DomainName = get_domain_name(HomePage)
QueueFile = Project_Name + '/queue.txt'
CrawledFile = Project_Name + '/crawled.txt'
ThreadsCount = 8
queue = Queue()
WebSpider(Project_Name, HomePage, DomainName)

def createWorkers():
    for _ in range(ThreadsCount):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        r = WebSpider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def createJobs():
    for link in fileToSet(QueueFile):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items in the queue, if so crawl them
def crawl():
        queued_links = fileToSet(QueueFile)
        if len(queued_links) != 0:
            print(str(len(queued_links)) + ' links in the queue')
            createJobs()
        
        

try:
    createWorkers()
    crawl()
except:
    print("Crawling done")
