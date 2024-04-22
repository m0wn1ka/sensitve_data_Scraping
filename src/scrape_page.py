from urllib.request import urlopen
import re
import base64
import json
def scrape_page(endpoint,subdomain):
    """
    i/p:takes endpoint as input
    uses requst module to get the content
    """
    print("in scraping  trying ",endpoint)
    if not endpoint:
        return
    try:
        page=urlopen(endpoint)
    except:
        return
    html_bytes=page.read()
    html=html_bytes.decode("utf-8")
    regex_phone=r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
    regex_email=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    mail_match=list(set(re.findall(regex_email,html)))
    phone_match=list(set(re.findall(regex_phone,html)))
    print("mail_mathc",mail_match,"phone match",phone_match)
    html=html.encode()#convert  into bytes
    encoded_html=base64.b64encode(html)
    print(type(encoded_html))
    scrape_page_dict={"page_url":endpoint,"web_page_content":encoded_html.decode(),"regex_filter_output":{"email_match":mail_match,"phone_match":phone_match}}
    with open("raw_output.json","r") as f:
        data=json.load(f)
        data["url_scan_results"]["subdomains"][-1]["webpages"].append(scrape_page_dict)
    with open("raw_output.json","w") as f:
        json.dump(data,f,indent=5)
        
    scrape_page_dict2={"page_url":endpoint,"regex_filter_output":{"email_match":mail_match,"phone_match":phone_match}}  
    with open("main_output.json","r") as f:
        data=json.load(f)
        data["url_scan_results"]["subdomains"][-1]["webpages"].append(scrape_page_dict2)
    with open("main_output.json","w") as f:
        json.dump(data,f,indent=5)
    
    
    
    
    