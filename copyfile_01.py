import shutil
import os
import pandas as pd 

#str匯入資料預處理
df = pd.read_csv(filename, index_col=0)
final_list = df.tolist()

#存放目標資料夾
dec=input('存放資料夾')
if not os.path.exists('newfolder'):
    print('已有此檔案夾請再確認')

def copyall(strall):
    for str in strall:
        shutil.copytree('str','dec')
    