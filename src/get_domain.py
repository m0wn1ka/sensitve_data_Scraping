from urllib.parse import urlparse
def get_domain(url):
    """
    i/p:url 
    o/p:domain
    used function/module:urllib built-in module
    """
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    print("domain (get_domain)",domain,"url is ",url)
    return domain