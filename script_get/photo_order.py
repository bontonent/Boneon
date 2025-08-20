#Photo_order.py create for create file for pull in DataBase
import pandas as pd
import os

def order(BASE_DIR):
    music_folder = (BASE_DIR.parent/"photo")
    i = 0
    df = pd.DataFrame(columns=["Articul", "PicName", "Type", "FileDescript", "Delete"])

    # Check file with jpg
    for root, dirs, files in os.walk(music_folder):
        for file in files:
            i += 1
            # File with jpg?
            if not file.endswith(".jpg"):
                continue
            # Correct name
            text = file.replace('.jpg', '')
            text_new = text
            if text.find("-kol-") != -1:
                text_new = text[:(text.find("-kol-"))]

            # Write data in row
            df.loc[i] = {
                'Articul': text_new,
                'PicName': text,
                'Type': 'jpg'
            }

    # Write all data what we have mined
    df.to_excel(BASE_DIR.parent/"pull_photo.xlsx", index=False)
    print("Write")
    df = pd.read_excel(BASE_DIR.parent/"pull_photo.xlsx")

    # If have element art_photo.xlsx
    try:
        df_file = pd.read_excel(BASE_DIR.parent/"art_photo.xlsx", sheet_name='Element', engine="openpyxl")
        df_ero = pd.read_excel(BASE_DIR.parent/"art_photo.xlsx", sheet_name='Error', engine="openpyxl")
        df_new = pd.DataFrame(columns=['Main num', 'Have?'])
        i = 0
        # Create name and write in file in such place
        for name in df.iloc[:,0]:
            i = i + 1
            bool_data = 'False'

            for art in df["Articul"]:
                if art.replace("DD ", '') == name.replace("DD ", ""):
                    bool_data = 'True'

            df_new.loc[i] = {
                'Main num': name,
                'Have?': bool_data
            }
        with pd.ExcelWriter(BASE_DIR.parent/'pull_photo.xlsx', engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name='втяжка', index=False)
            df_new.to_excel(writer, sheet_name='have', index=False)
            df_ero.to_excel(writer, sheet_name='Error', index=False)
    # Write all
    except FileNotFoundError:
        print("Don't have art_photo.xlsx-")
        pass
    finally:
        print("finished")
    return BASE_DIR