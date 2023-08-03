import pandas as pd
from bs4 import BeautifulSoup as beauty
import requests

#home url of the category we need
url="https://www.jumia.co.ke/computing/"
#url="https://www.jumia.co.ke/phones-tablets/"
all_url=[] #list to hold all URLs

#fetching all URLs page by page
for page in range (1,2):
    next_url=url+"?page="+str(page)+"#catalog-listing"
    #print(next_url)
    all_url.append(next_url)
    
#searching the URLs
for url in all_url:
    render=requests.get(url)
    the_html=beauty(render.content,"html.parser")
    #print(the_html)
    scrape=the_html.find_all(class_="name")
    #print(scrape)
    scraped_data=[]
    for data in scrape:
        scraped_data.append(data.get_text())
        cleaned_data=[data.replace("\n","") for data in scraped_data]#remove new line
        clean_data_=[data.replace("    ","") for data in scraped_data]#remove space
        #print(clean_data_)
        data_2_csv=pd.DataFrame(clean_data_,columns=["column"])
        data_2_csv.to_csv("jumia.csv",mode="a",index=False)
        print(data_2_csv)