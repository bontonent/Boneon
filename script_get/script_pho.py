import os
import sys
import pandas as pd
import photo_one
import delete_copy
try:
    from scrapy.crawler import CrawlerProcess
    from script_get.spiders.shop import ShopSpider

    from scrapy.settings import Settings
    import script_get.settings as project_settings
except:
    import PyQt6
    from PyQt6 import QtWidgets

    app = QtWidgets.QApplication([])

    error_dialog = QtWidgets.QErrorMessage()
    error_dialog.setWindowTitle("Error")
    error_dialog.showMessage("Don't have VPN!")
    app.exec()
    print("Need VPN")

def script_get(BASE_DIR, num1, num2):
    BASE_DIR1 = BASE_DIR/"script_get"
    os.chdir(BASE_DIR/"script_get")
    number1 = int(num1)
    number2 = int(num2)
    print(number1)

    df = pd.DataFrame(columns=['number'])
    df.loc[len(df)] = {'number': number1}
    df.loc[len(df)] = {'number': number2}
    try:
        if (int(number1) == 0) & (int(number2) == 1):
            BASE_DIR1 = photo_one.get_photo(BASE_DIR1)
        # Run the spider named 'shop'
        else:
            settings = Settings()
            settings.setmodule(project_settings)
            process = CrawlerProcess(settings=settings)
            process.crawl(ShopSpider)
            process.start()
            BASE_DIR1 = BASE_DIR
            os.chdir(BASE_DIR1)
    except Exception as e:
        print(e)
    finally:
        print("Finished")
        try:
            delete_copy.del_cop(BASE_DIR)
        except Exception as e:
            print(e)
    return BASE_DIR1