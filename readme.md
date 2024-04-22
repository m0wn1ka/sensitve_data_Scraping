## web scraping 
- this appplication takes a file of urls in a csv file
- finds domain of each url
- for each ulr finds subdomanis
- for each subdomain finds the endpoints 
- gets and stores the base64  encoded content of the endpoint
- greps for emails,phones numbers
## output format
- output is stored in output folder
- mailny in 3 json files the output is stored
- main_output.json contains the main output
- raw_output.json contains the raw output along with the base64 encoded data
- regex_output.json has the matched emails and phone numbers
- the above will be created for each url in the provided csv file
## setup and usage
- install the requirements
- mention the urls in urls.csv file 
- run `python3 main.py`
