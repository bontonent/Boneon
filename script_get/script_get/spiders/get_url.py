## Script for get data from Json file. With algorithm create url
from pydoc import replace
import requests
import json

def get(code):
    url_end = ""
    # search in web-site with code
    url = f"https://shop.deere.com/bff/v1/search?query={code}&page=1&size=24&productType=all&countryCode=US"
    payload = json.dumps({
      "facets": [],
      "sortParam": "RELEVANCE",
      "nonOnBoardedDealer": False,
      "enableQueryCorrection": True
    })
    # headers from web-site
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
    #connect json element from site
    response = requests.request("POST", url, headers=headers, data=payload)
    label_keys = response.json()
    #get element name for create url
    for key in label_keys["products"]:
        if key["code"] == code:
            keycode = key["name"]
            # Create url
            code_space = "".join((code,":"))
            code_space_2 = "".join((code, ": "))
            keycode_url = ("".join((replace(replace(replace(keycode,code_space,""), " ", "-"),",","%2C"),f"/p/{code}"))).replace("(","-").replace(")","-")
            end_url = "".join((code,"%3A",keycode_url))
            url_end = "".join(("https://shop.deere.com/us/product/",end_url))
    # return url
    return url_end
