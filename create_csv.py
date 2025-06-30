from pathlib import Path
import pandas as pd
import os
BASE_DIR = Path(__file__).resolve().parent/"script_get"
BASE_DIR1 = BASE_DIR
os.chdir(BASE_DIR1)

df  = pd.DataFrame(columns = ['number'])

# df = pd.read_pickle(BASE_DIR1/'./temp/num.csv')
number1 = 0
number2 = 2
# create data
df.loc[len(df)] = {'number': number1}
df.loc[len(df)] = {'number': number2}
# data to csv file
df.to_csv(BASE_DIR1/'temp/num.csv')

#print(df.head())


