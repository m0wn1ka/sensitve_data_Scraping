import subprocess
def get_subdomains(domain):
    """
    ip:takes a domain
    o/p:returns the the list of subdomains
    intermediate:uses subfinder to get list of them
    write them to subdomains.txt file for further use
    append domain to list of subdomains"""
    print("in get subdomains function")
    sub_domain_file=domain+"subdomains.txt"
    subprocess.run(["subfinder","-d",domain,"-o",sub_domain_file],shell=True,capture_output=True)
    with open(sub_domain_file,"r") as file:
        sub_domain_list=file.read().split("\n")
        if(domain not in sub_domain_list):  
            sub_domain_list.append(domain)
    with open(sub_domain_file,"a") as file:
        file.write("\n")
        file.write(domain)
    return sub_domain_list
 