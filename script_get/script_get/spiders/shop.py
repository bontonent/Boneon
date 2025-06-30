import scrapy
import pandas as pd
import requests
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
# good work themselves in scrapy crawl shop
#from script_get.spiders import get_url
from script_get.spiders import get_url
print(BASE_DIR)
BASE_DIR1 = BASE_DIR.parent.parent
## get new excel file(of if you don't want remove past excel)
#df = pd.DataFrame(
#    columns=['code', 'name', 'ungroup', 'group', 'weight', 'height', 'width', 'length', 'volume', 'describe', 'model'])
#df.to_excel('work.xlsx', index=False)

df_csv = pd.read_csv(BASE_DIR1/"temp/num.csv")
BASE_DIR = BASE_DIR.parent
df_get = pd.read_excel(BASE_DIR.parent/"art_photo.xlsx", sheet_name = 'Element', engine="openpyxl")

error_element = []
try:
    df_error = pd.read_excel(BASE_DIR.parent/"art_photo.xlsx", sheet_name = 'Error', engine="openpyxl")
    error_element = df_error['error']
except:
    df_error = pd.DataFrame(columns=['error'])
i = -1
while i < len(df_get) - 1:
    print(i + 2, " ", len(df_get), " ", int(((i + 2) / len(df_get))))
    next_page = get_url.get(df_get['Main num'][i + 1])
    if next_page == "":
        print("skip")
        i = i + 1
    else:
        i = i + 1
        code = (df_get['Main num'][i])
        break

url_element = get_url.get(code)
if url_element == "":
    print("don't have")


class ShopSpider(scrapy.Spider):
    name = "shop"
    allowed_domains = ["shop.deere.com"]
    start_urls = [url_element]
    handle_httpstatus_list = [400, 403, 404, 500]

    def __init__(self):
        self.i = i
        df_csv = pd.read_csv(BASE_DIR1/"temp/num.csv")
        self.num1 = df_csv['number'][0]
        self.num2 = df_csv['number'][1]


    def parse(self, response):
        if response.status != 400 and response.status != 404 and response.status != 500 and response.status != 403:
            photos = response.css('ul.thumbs.animated li img::attr(src)').getall()
            u = 0
            for photo in photos:
                temp = "".join(("DD ", df_get['Main num'][self.i], "-kol-", str(u)))
                if u < int(self.num1):
                    u = u + 1
                    continue
                u = u + 1
                # max element
                if u > int(self.num2):
                    break
                print(photo)
                url = requests.get(photo)
                f"./../photo/DD {code}.jpg"
                with open(BASE_DIR.parent/f"photo/{str(temp)}.jpg", 'wb') as f:
                    f.write(url.content)
            # while if don't end element
            while self.i < len(df_get)-1:
                print(self.i+2, " ", len(df_get)," ", int(((self.i+2)/len(df_get))*100))
                next_page = get_url.get(df_get['Main num'][self.i + 1])
                if next_page == "":
                    print("skip")
                    self.i = self.i + 1
                else:
                    self.i = self.i + 1
                    yield response.follow(next_page, callback=self.parse)
                    break

            with pd.ExcelWriter(BASE_DIR.parent/"art_photo.xlsx") as writer:
                df_get.to_excel(writer, sheet_name='Element', index=False)
                df_error.to_excel(writer, sheet_name='Error', index=False)
        else:
            df_error.loc[len(df_error)] = {'error' : df_get['Main num'][self.i]}
            while self.i < len(df_get) - 1:
                print(self.i + 2, " ", len(df_get), " ", int(((self.i + 2) / len(df_get))))
                next_page = get_url.get(df_get['Main num'][self.i + 1])
                if next_page == "":
                    print("skip")
                    self.i = self.i + 1
                else:
                    self.i = self.i + 1
                    yield response.follow(next_page, callback=self.parse)
                    break
