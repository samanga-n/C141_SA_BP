from selenium import webdriver
# from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Chrome("C:\Users\Sreekesh\Desktop\WHJ\PYTHON\1on4\C141\C141TA\chromedriver.exe")

browser.get(START_URL)
time.sleep(10)


def scrape():
    
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    
    planets_data = []

    for i in range(0,490):
        
        soup = BeautifulSoup(browser.page_source, "html.parser")
        # print(f'Scrapping page {i+1} ...' )
        
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):

            li_tags = ul_tag.find_all("li")
            temp_list = []

            for index, li_tag in enumerate(li_tags):

                if index == 0:                   
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")

            planets_data.append(temp_list)
    print(planets_data[1])