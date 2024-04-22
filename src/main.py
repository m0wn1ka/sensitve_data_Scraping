import csv
import os
import subprocess
import json
from url_func import url_func 
#reading csv file and going through each line
with open("urls.csv","r") as file:
    reader=csv.reader(file)
    os.mkdir("output")
    os.chdir("output")  
   
    for line in reader:
        for url in line:
            if url:
                url_func(url)
                print("done with ",url)
                emails=[]
                phones=[]
                with open("main_output.json","r") as f:
                    data1=json.load(f)
                #getting emails and phones start
                x=data1["url_scan_results"]["subdomains"]
                for i in x:
                    webpages=i["webpages"]
                    for webpage in webpages:
                        filter_output=webpage["regex_filter_output"]
                        emails.append(filter_output["email_match"])
                        phones.append(filter_output["phone_match"])
                new_emails=[]
                for p in emails:
                    if p in new_emails:
                        pass
                    else:
                        new_emails.append(p)
                new_phones=[]
                for p in phones:
                    if p in new_phones:
                        pass
                    else:
                        new_phones.append(p)
                phones=new_phones
                emails=new_emails
                    
                        
                # end 
                with open("regex_output.json","w") as f:
                    data2_dict={"url_scan_results":{
                        "url":url,
                        "domain":data1["url_scan_results"]["domain"],
                        "combinedRegexOutput": {
                            "email_addresses":((emails)),
                            "phones":((phones))
                        }
                    }}
                    json.dump(data2_dict,f,indent=5)
            os.chdir("..")        
                
            
                            
            