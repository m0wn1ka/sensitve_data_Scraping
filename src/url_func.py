from get_domain import get_domain
import json
import os
import subprocess
from get_subdomains import get_subdomains
from subdomain_func import subdomain_func
def url_func(url):
    """
    this function will be called on each url
    i/p:takes the url as input
    """
    domain=get_domain(url)
    print("domain is ",domain)
    os.mkdir(domain)
    os.chdir(domain)
    # with open("katana.txt","w") as f:
    #     f.write("https://radha-m0wn1ka.github.io/posts/test")
    with open("raw_output.json","w") as f:
        pass
    with open("main_output.json","w") as f:
        pass
    with open("regex_output.json","w") as f:
        pass
    with open("raw_output.json","a") as f:                    
        dict1={"url_scan_results":{"url":url,"domain":domain,"subdomains":[]}}
        json.dump(dict1,f)
    with open("main_output.json","a") as f:                    
        dict1={"url_scan_results":{"url":url,"domain":domain,"subdomains":[]}}
        json.dump(dict1,f)
    subdomain_list=get_subdomains(domain)
    i=1
    for subdomain in subdomain_list:
        if(subdomain):
            subdomain_func(subdomain)
            i+=1
        if(i>=3):
            break