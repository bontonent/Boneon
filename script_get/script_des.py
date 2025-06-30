# Script_des.py created for create describe.xlsx with data
# You describe same elements on photo_one
import os
# launch specific library.
try:
    from scrapy.crawler import CrawlerProcess
    from script_get.spiders.describe import DescribeSpider
    # horrible Settings(a lot of error from him)
    from scrapy.settings import Settings
    import script_get.settings as project_settings
except:
    # Without notify on screen because we don't need it twith
    print("Need VPN")

def get_des(BASE_DIR):
    #work directory
    BASE_DIR1 = BASE_DIR / "script_get"
    os.chdir(BASE_DIR1)
    #call all data
    settings = Settings()
    settings.setmodule(project_settings)
    process = CrawlerProcess(settings=settings)
    process.crawl(DescribeSpider)
    process.start()
    # Reset directory
    os.chdir(BASE_DIR/".")

