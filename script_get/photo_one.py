import requests
import json
import pandas as pd
import time
import os

def get_photo(BASE_DIR):
    BASE_DIR1 = BASE_DIR.parent
    os.chdir(BASE_DIR1)
    df = pd.read_excel(BASE_DIR1.parent/"art_photo.xlsx", sheet_name="Element", engine="openpyxl")

    for form in range(len(df[:])):
        print(form + 1," ",len(df))
        try:
            code = df['Main num'][form]
            url_end = ""
            url = f"https://shop.deere.com/bff/v1/search?query={code}&page=1&size=24&productType=all&countryCode=US"

            print(code)
            payload = json.dumps({
                "facets": [],
                "sortParam": "RELEVANCE",
                "nonOnBoardedDealer": False,
                "enableQueryCorrection": True
            })
            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US',
                'content-type': 'application/json',
                'custom-header': 'custom',
                'journey-id': '8e0faebf-82c2-4364-8836-5096551cdf23',
                'origin': 'https://shop.deere.com',
                'priority': 'u=1, i',
                'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
                'Cookie': 'us-uc-cart-id=832d0272-174e-4892-8f4f-f7649d072236; AMCV_8CC867C25245ADC30A490D4C%40AdobeOrg=MCMID|15080590552696746783908146833337164326; ConstructorioID_client_id=8ce9bdf6-3409-44b6-8012-7e16a6a465fc; __stripe_mid=8482c0d9-d44a-4471-8c61-9edfc7f8690e6ccf3f; _gcl_au=1.1.191061507.1745822146; _fbp=fb.1.1745822146975.120575221724790983; kndctr_8CC867C25245ADC30A490D4C_AdobeOrg_consent=general%3Din; ConstructorioID_client_id=8ce9bdf6-3409-44b6-8012-7e16a6a465fc; JSESSIONID=967C5E2D6648209C8CC7C1A60B142144; kndctr_8CC867C25245ADC30A490D4C_AdobeOrg_cluster=irl1; kndctr_8CC867C25245ADC30A490D4C_AdobeOrg_identity=CiYxNTA4MDU5MDU1MjY5Njc0Njc4MzkwODE0NjgzMzMzNzE2NDMyNlIRCJa17djnMhgBKgRJUkwxMAHwAe%2D4z5TtMg%3D%3D; ConstructorioID_session_id=21; __stripe_sid=13b5f9ef-337c-4fd8-967a-4b5bcd635a21f73058; AWSALB=FCfeeIrW33yDGef01JpMISLsRodlsEIWo4c4lQ9D1gfN5uICRRwvN0xijd7Its9FJN6LhF/QMp1hOcN98Jl7Jq4eBTfZJJetRFaNvi3YCHlon6ldEDu5YWWAlv05; AWSALBCORS=FCfeeIrW33yDGef01JpMISLsRodlsEIWo4c4lQ9D1gfN5uICRRwvN0xijd7Its9FJN6LhF/QMp1hOcN98Jl7Jq4eBTfZJJetRFaNvi3YCHlon6ldEDu5YWWAlv05; cartUserId=YW5vbnltb3Vz; ConstructorioID_session={"sessionId":21,"lastTime":1747289810380}; OptanonConsent=isGpcEnabled=0&datestamp=Thu+May+15+2025+09%3A16%3A50+GMT%2B0300+(Eastern+European+Summer+Time)&version=202503.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=621e33ca-087d-4819-a7ac-0bc17a2c3d28&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false; _dd_s=rum=1&id=4aba1d19-2f3c-4924-9388-0a35c2dd9a6d&created=1747289628806&expire=1747290710420',
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            work = response.json()

            values = "None"
            for key in work["products"]:
                if key["code"] == code:
                    values = "Don't have photo"
                    keycode = key["code"]
                    for kol in key['assets']:
                        if kol["resolution"] == '1200Wx1200H':
                            print(kol['url'])
                            url = kol['url']
                            response = requests.get(url)
                            with open(BASE_DIR1.parent/f"photo/DD {code}-kol-0.jpg",
                                                           "wb") as f:
                                                     f.write(response.content)
        except Exception:
            time.sleep(10)
            url = f"https://shop.deere.com/bff/v1/search?query={code}&page=1&size=24&productType=all&countryCode=US"

            print(code)
            payload = json.dumps({
                "facets": [],
                "sortParam": "RELEVANCE",
                "nonOnBoardedDealer": False,
                "enableQueryCorrection": True
            })
            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US',
                'content-type': 'application/json',
                'custom-header': 'custom',
                'journey-id': '8e0faebf-82c2-4364-8836-5096551cdf23',
                'origin': 'https://shop.deere.com',
                'priority': 'u=1, i',
                'referer': f'https://shop.deere.com/us/search?text={code}&productType=all',
                'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
                'Cookie': 'kndctr_8CC867C25245ADC30A490D4C_AdobeOrg_identity=CiY4ODQ4NDg2NzQzMTc3MzgxMDA3MjQwOTQyNDczMjA4ODc5NTE3M1ITCI%5FGmsvjMhABGAEqBElSTDEwAPABj8aay%2DMy; AMCV_8CC867C25245ADC30A490D4C%40AdobeOrg=MCMID|88484867431773810072409424732088795173; us-uc-cart-id=05ba1c49-8cad-4ea2-9c13-b67dca1dc273; ConstructorioID_client_id=06d715d2-653f-4382-b311-5c8f864f8d1b; ConstructorioID_client_id=06d715d2-653f-4382-b311-5c8f864f8d1b; __stripe_mid=ee409f60-4901-4799-b02f-3e95a96c4512d6b643; _gcl_au=1.1.343342310.1744783029; JSESSIONID=0B94A2B00F25B04DC67BBBAFF64E766D; kndctr_8CC867C25245ADC30A490D4C_AdobeOrg_cluster=irl1; ConstructorioID_session_id=6; __stripe_sid=f7aa7689-3773-44ac-a186-228d576664a4522eff; AWSALB=6bSb9HpZ0U+9SHWj4DDNn7fb6PkXtxa5uc9VgLO8eJfgbFEOPQkl2Dt+gsJ4zSkp35al9yPfR99t9JK8DOD46EBwKEuIH16LtfESGqbvQHeg/STotBaF1UgWMtoS; AWSALBCORS=6bSb9HpZ0U+9SHWj4DDNn7fb6PkXtxa5uc9VgLO8eJfgbFEOPQkl2Dt+gsJ4zSkp35al9yPfR99t9JK8DOD46EBwKEuIH16LtfESGqbvQHeg/STotBaF1UgWMtoS; cartUserId=YW5vbnltb3Vz; ConstructorioID_session={"sessionId":6,"lastTime":1744794487434}; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Apr+16+2025+12%3A08%3A07+GMT%2B0300+(%D0%B7%D0%B0+%D1%81%D1%85%D1%96%D0%B4%D0%BD%D0%BE%D1%94%D0%B2%D1%80%D0%BE%D0%BF%D0%B5%D0%B9%D1%81%D1%8C%D0%BA%D0%B8%D0%BC+%D0%BB%D1%96%D1%82%D0%BD%D1%96%D0%BC+%D1%87%D0%B0%D1%81%D0%BE%D0%BC)&version=202503.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=82e127cd-477c-4ae6-be25-383a221aa7c9&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            work = response.json()
            for key in work["products"]:
                if key["code"] == code:
                    values = "Don't have photo"
                    keycode = key["code"]
                    for kol in key['assets']:
                        if kol["resolution"] == '1200Wx1200H':
                            print(kol['url'])
                            url = kol['url']
                            response = requests.get(url)
                            with open(BASE_DIR1.parent/f"photo/DD {code}-kol-0.jpg",
                                      "wb") as f:
                                f.write(response.content)