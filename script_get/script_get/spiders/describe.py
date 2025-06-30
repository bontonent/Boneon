from openpyxl import load_workbook
import scrapy
import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
# good work themselves in scrapy crawl shop
from script_get.spiders import get_url
BASE_DIR1 = BASE_DIR
## get new excel file(of if you don't want remove past excel)
df_get = pd.read_excel(BASE_DIR.parent.parent/"art_photo.xlsx", sheet_name = 'Element', engine="openpyxl")

## get new excel file(of if you don't want remove past excel)
df = pd.DataFrame(
    columns=['code', 'name', 'ungroup', 'group', 'weight', 'height', 'width', 'length', 'volume', 'describe', 'model'])
df.to_excel(BASE_DIR.parent.parent/'describe.xlsx', index=False)
error_element = []
try:
    df_error = pd.read_excel(BASE_DIR.parent.parent/"describe.xlsx", sheet_name = 'Error', engine="openpyxl")
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

class DescribeSpider(scrapy.Spider):
    name = "describe"
    allowed_domains = ["shop.deere.com"]
    start_urls = [url_element]
    handle_httpstatus_list = [400, 403, 404, 500]

    ##start element for 1, 2, 3 . . .
    def __init__(self):
        self.i = i

    def parse(self, response):
        if response.status != 400 and response.status != 404 and response.status != 500 and response.status != 403:
            ##weight zero element(if don't have, get Nothing
            des_tem = ""
            weight = ""
            height = ""
            width = ""
            length = ""
            volume = ""
            mod_tem = ""
            new_code = ""
            new_name = ""
            new_ungroop = ""
            new_group = ""
            ##nums
            nums = response.css('li.MuiBreadcrumbs-li span::attr(data-text)')

            ##weight
            sizes = response.css('body div div main section div div div div div div div div div div::text').getall()
            for size in range(len(sizes)):
                if sizes[size] == "Weight":
                    weight = sizes[size + 1]
                if sizes[size] == "Height":
                    height = sizes[size + 1]
                if sizes[size] == "Width":
                    width = sizes[size + 1]
                if sizes[size] == "Length":
                    length = sizes[size + 1]
                if sizes[size] == "Volume":
                    volume = sizes[size + 1]
            ##describe
            describes = response.css(
                'body div div main section div div div ul.MuiTypography-root.MuiTypography-body1 li::text').getall()
            for describe in describes[:]:
                if des_tem == "":
                    des_tem = "".join((des_tem, describe))
                des_tem = "".join((des_tem, "!!!", describe))
            # Create Models
            work_station = ""
            scripts = response.css("script::text").getall()
            for script in scripts:
                if -1 != script.find("window.initializedProductDetailsData"):                work_station = script

            work_start = work_station[work_station.find('models'):]
            mod_tem =  work_start[:work_start.find('}')].replace('models":[', "").replace(']', "").replace(',', "!!!").replace('"', "")

            new_code = nums[3].get()[:nums[3].get().find(':')]
            new_name = nums[3].get().replace("".join((nums[3].get()[:nums[3].get().find(':')], ": ")), "")
            new_ungroup = nums[2].get()
            new_group = nums[1].get()
            ##add all elements in pd
            new_row = pd.DataFrame([{
                'code': new_code,
                'name': new_name,
                'ungroup': new_ungroup,
                'group': new_group,
                'weight': weight,
                'height': height,
                'width': width,
                'length': length,
                'volume': volume,
                'describe': des_tem,
                'model': mod_tem
            }])
            ##save data in excel file
            art = load_workbook(BASE_DIR.parent.parent/"describe.xlsx")
            writer = pd.ExcelWriter(BASE_DIR.parent.parent/'describe.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay')
            writer.art = art
            startrow = writer.art.active.max_row
            new_row.to_excel(writer, index=False, header=False, startrow=startrow)
            writer._save()
            writer.close()
            ##go to next element
            while self.i < len(df_get) - 1:
                print(self.i + 2, " ", len(df_get), " ", int(((self.i + 2) / len(df_get))))
                next_page = get_url.get(df_get['Main num'][self.i + 1])
                if next_page == "":
                    print("skip")
                    self.i = self.i + 1
                else:
                    self.i = self.i + 1
                    yield response.follow(next_page, callback=self.parse,
                                          cookies={'us-uc-cart-id': '832d0272-174e-4892-8f4f-f7649d072236',
                                                   'AMCV_8CC867C25245ADC30A490D4C%40AdobeOrg': 'MCMID|15080590552696746783908146833337164326',
                                                   'ConstructorioID_client_id': '8ce9bdf6-3409-44b6-8012-7e16a6a465fc',
                                                   '_gcl_au': '1.1.191061507.1745822146',
                                                   '_fbp': 'fb.1.1745822146975.120575221724790983',
                                                   'kndctr_8CC867C25245ADC30A490D4C_AdobeOrg_consent': 'general%3Din',
                                                   'kndctr_8CC867C25245ADC30A490D4C_AdobeOrg_cluster': 'irl1',
                                                   'kndctr_8CC867C25245ADC30A490D4C_AdobeOrg_identity': 'CiYxNTA4MDU5MDU1MjY5Njc0Njc4MzkwODE0NjgzMzMzNzE2NDMyNlIRCJa17djnMhgBKgRJUkwxMAHwAe%2D4z5TtMg%3D%3D',
                                                   'ConstructorioID_session_id': '21',
                                                   'ConstructorioID_session': '{"sessionId":21,"lastTime":1747290931769}'
                                                   })
                    break
        else:
            # if error element say error
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
    ## weight element get