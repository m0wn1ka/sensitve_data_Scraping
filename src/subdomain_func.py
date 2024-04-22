import subprocess
from scrape_page import scrape_page
import json

def subdomain_func(subdomain):
    """
    i/p:takes each subdomain as input
    intermediate:uses katana and stores in katana.txt file
    then for each endpoint call scrape_page function 
    """
    with open("raw_output.json","r") as f:
            data=json.load(f)
            dict_sub={"subdomain":subdomain,"webpages":[]}
            data["url_scan_results"]["subdomains"].append(dict_sub)
    with open("raw_output.json","w") as f:
        json.dump(data,f)
    with open("main_output.json","r") as f:
            data=json.load(f)
            dict_sub={"subdomain":subdomain,"webpages":[]}
            data["url_scan_results"]["subdomains"].append(dict_sub)
    with open("main_output.json","w") as f:
        json.dump(data,f)
    katana_file="katana.txt"
    
    subprocess.run(["katana","-u",subdomain,"-o",katana_file,"-d","2"])   
    with open(katana_file,"r") as file:
        x=file.read().split("\n")
        print("got endpoints are ",x,"for subdomain ",subdomain)
    p=1
    for endpoint in x:
        print("calldin scrape page with ",endpoint)
        
        scrape_page(endpoint,subdomain)
        p+=1
        if(p>=3):
            break