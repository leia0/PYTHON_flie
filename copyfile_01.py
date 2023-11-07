import shutil
import pandas as pd 

#str匯入資料預處理
df = pd.read_csv(filename, index_col=0)
final_list = df.tolist()

#帶入自訂dec_file模組方法


#篩選複製檔案
def copyall(strall):
    for str in strall:
        shutil.copytree('str','dec')
    