# Shop.py for get photo 2 or more(We can get only 1 photo, but it is bad idea, very long)
# a lot of same with describe
import scrapy
import pandas as pd
import requests
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
# good work themselves in scrapy crawl shop
from script_get.spiders import get_url
print(BASE_DIR)
BASE_DIR1 = BASE_DIR.parent.parent
# get data first and last numbers photo
df_csv = pd.read_csv(BASE_DIR1/"temp/num.csv")
BASE_DIR = BASE_DIR.parent

## get new excel file(of if you don't want remove past excel)
df_get = pd.read_excel(BASE_DIR.parent.parent/"art_photo.xlsx", sheet_name = 'Element', engine="openpyxl")
# Get excel, and error past elment
error_element = []
try:
    df_error = pd.read_excel(BASE_DIR.parent.parent/"art_photo.xlsx", sheet_name = 'Error', engine="openpyxl")
    error_element = df_error['error']
except:
    df_error = pd.DataFrame(columns=['error'])
# Check all articles, what have in Shop Deere
i = -1
while i < len(df_get) - 1:
    print(i + 2, "/", len(df_get))
    next_page = get_url.get(df_get['Main num'][i + 1])
    if next_page == "":
        print("skip")
        i = i + 1
    else:
        i = i + 1
        code = (df_get['Main num'][i])
        break
# With past step we know, we get url for url_element
url_element = get_url.get(code)
if url_element == "":
    # If None element we haven't
    print("don't have")


class ShopSpider(scrapy.Spider):
    #name
    name = "shop"
    #domen
    allowed_domains = ["shop.deere.com"]
    # Url work scrapy
    start_urls = [url_element]
    # Can be error
    handle_httpstatus_list = [400, 403, 404, 500]

    def __init__(self):
        # always understand what we check element
        self.i = i
        df_csv = pd.read_csv(BASE_DIR1/"temp/num.csv")
        # always need know first and last photo element
        self.num1 = df_csv['number'][0]
        self.num2 = df_csv['number'][1]


    def parse(self, response):
        # can be error
        if response.status != 400 and response.status != 404 and response.status != 500 and response.status != 403:
            # script get url photos
            photos = response.css('ul.thumbs.animated li img::attr(src)').getall()
            u = 0
            # (write script)
            for photo in photos:
                temp = "".join(("DD ", df_get['Main num'][self.i], "-kol-", str(u)))
                # first element can be 0 1.. and we start with it is element
                if u < int(self.num1):
                    u = u + 1
                    continue
                # add
                u = u + 1
                # max element check, if don't have we continue get data
                if u > int(self.num2):
                    break
                # get data
                print(photo)
                url = requests.get(photo)
                f"./../photo/DD {code}.jpg"
                with open(BASE_DIR.parent.parent/f"photo/{str(temp)}.jpg", 'wb') as f:
                    f.write(url.content)
            # while if don't end element
            # go next element
            while self.i < len(df_get)-1:
                print(self.i+2, "/", len(df_get))
                next_page = get_url.get(df_get['Main num'][self.i + 1])
                if next_page == "":
                    print("skip")
                    self.i = self.i + 1
                else:
                    self.i = self.i + 1
                    yield response.follow(next_page, callback=self.parse)
                    break
            with pd.ExcelWriter(BASE_DIR.parent.parent/"art_photo.xlsx") as writer:
                df_get.to_excel(writer, sheet_name='Element', index=False)
                df_error.to_excel(writer, sheet_name='Error', index=False)
        # add data to excel Error
        else:
            # if error element say error. Here have write error element(in describe don't have)
            df_error.loc[len(df_error)] = {'error' : df_get['Main num'][self.i]}
            while self.i < len(df_get) - 1:
                print(self.i + 2, "/", len(df_get))
                next_page = get_url.get(df_get['Main num'][self.i + 1])
                if next_page == "":
                    print("skip")
                    self.i = self.i + 1
                else:
                    self.i = self.i + 1
                    yield response.follow(next_page, callback=self.parse)
                    break
