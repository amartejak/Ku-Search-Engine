from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, baseUrl, pageUrl):
        super().__init__()
        self.baseUrl = baseUrl
        self.pageUrl = pageUrl
        self.links = set()

    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handleStarttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.baseUrl, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass
