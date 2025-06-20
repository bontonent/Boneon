# Scrapy settings for script_get project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "script_get"

SPIDER_MODULES = ["script_get.spiders"]
NEWSPIDER_MODULE = "script_get.spiders"

ADDONS = {}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "script_get (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
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

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "script_get.middlewares.ScriptGetSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "script_get.middlewares.ScriptGetDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "script_get.pipelines.ScriptGetPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"
