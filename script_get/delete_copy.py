# Delete_copy created for delete all copy in Art_photo Sheet Error
import pandas as pd
import numpy as np
# create main def
def del_cop(BASE_DIR):
    #get data from sheet
    df = pd.read_excel(BASE_DIR.parent/'art_photo.xlsx', sheet_name='Error', engine='openpyxl')
    element = []
    # make column without copy
    for big_error in df.iloc[:,0]:
        index = True
        for new_error in element:
            if str(big_error) == str(new_error):
                index = False
        if index:
            element.append(big_error)
    # Add data in sheet(don't forgot about Element sheet)
    data = np.array(element)
    df_new = pd.DataFrame(data,columns = ['error'])
    df_1 = pd.read_excel(BASE_DIR.parent/'art_photo.xlsx', sheet_name='Element', engine='openpyxl')

    with pd.ExcelWriter(BASE_DIR.parent/"art_photo.xlsx", engine='openpyxl') as writer:
        df_1.to_excel(writer, sheet_name='Element', index=False)
        df_new.to_excel(writer, sheet_name='Error', index=False)