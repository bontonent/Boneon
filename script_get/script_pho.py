# Script_pho.py create for call scrapy(2 or more photo) or request(1 photo)
import os
import sys
import pandas as pd
import photo_one
import delete_copy
# launch specific library.
try:
    from scrapy.crawler import CrawlerProcess
    from script_get.spiders.shop import ShopSpider
    # horrible Settings(a lot of error from him)
    from scrapy.settings import Settings
    import script_get.settings as project_settings
except:
    # if Error you don't have VPN
    import PyQt6
    from PyQt6 import QtWidgets

    app = QtWidgets.QApplication([])

    error_dialog = QtWidgets.QErrorMessage()
    error_dialog.setWindowTitle("Error")
    error_dialog.showMessage("Don't have VPN!")
    app.exec()
    print("Need VPN")

def script_get(BASE_DIR, num1, num2):
    # directory where we
    BASE_DIR1 = BASE_DIR/"script_get"
    os.chdir(BASE_DIR/"script_get")
    # get data for choose what we should using
    number1 = int(num1)
    number2 = int(num2)
    df = pd.DataFrame(columns=['number'])
    df.loc[len(df)] = {'number': number1}
    df.loc[len(df)] = {'number': number2}
    # try run
    try:
        # only one photo
        if (int(number1) == 0) & (int(number2) == 1):
            BASE_DIR1 = photo_one.get_photo(BASE_DIR1)
        # two photo or more
        else:
            settings = Settings()
            settings.setmodule(project_settings)
            process = CrawlerProcess(settings=settings)
            process.crawl(ShopSpider)
            process.start()
            BASE_DIR1 = BASE_DIR
            os.chdir(BASE_DIR1)
    # if error notify me
    except Exception as e:
        print(e)
    finally:
        # end work
        print("Finished")
        try:
            # delete all copy from Error Sheet
            delete_copy.del_cop(BASE_DIR)
        except Exception as e:
            print(e)
    return BASE_DIR1