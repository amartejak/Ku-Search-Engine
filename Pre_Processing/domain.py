from urllib.parse import urlparse

def getDomainName(url):
    try:
        results = getSubDomainName(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

def getSubDomainName(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
