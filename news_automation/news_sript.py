from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.chrome.options import Options



options=Options()
options.add_argument('--headless') #enable it for headless mode

website='https://stockmarket.com/'
path='chromedriver.exe'

service=Service(path)
wbdriver=webdriver.Chrome(service=service,options=options)
wbdriver.get(website)



container=wbdriver.find_elements(by='xpath',value="//div[@class='archive-main']/article")



title=[]
subtitle=[]
author=[]
link=[]



for element in container:
    title1=element.find_element(by='xpath',value=".//div[@class='entry-data']/header/h2").text
    subtitle1=element.find_element(by='xpath',value=".//div[@class='entry-data']/div[@class='entry-excerpt']").text
    author1=element.find_element(by='xpath',value=".//div[@class='entry-data']/ul/li[1]/span/a").text
    link1=element.find_element(by='xpath',value=".//div[@class='post-outer']/a[1]").get_attribute("href")
    title.append(title1)
    subtitle.append(subtitle1)
    author.append(author1)
    link.append(link1)
    print(title1)
    print("*"*10)

    
df=pd.DataFrame({'title':title,'subtitle':subtitle,'author':author,'link':link})

df.to_csv("news.csv")


wbdriver.quit()
