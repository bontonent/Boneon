import os
try:
    from scrapy.crawler import CrawlerProcess
    from script_get.spiders.describe import DescribeSpider

    from scrapy.settings import Settings
    import script_get.settings as project_settings
except:
    print("Need VPN")
#from script_get.spiders.shop import ExampleSpider

def get_des(BASE_DIR):
    BASE_DIR1 = BASE_DIR / "script_get"
    os.chdir(BASE_DIR1)
    settings = Settings()
    settings.setmodule(project_settings)
    process = CrawlerProcess(settings=settings)
    process.crawl(DescribeSpider)
    process.start()

    os.chdir(BASE_DIR/".")

