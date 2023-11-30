'''模組與套件說明
模組名稱就是一個檔案名稱
套件名稱是資料夾名稱
*from 模組名稱 import 方法名稱
*from 第2層資料夾名稱 import 模組名稱
'''

#顯示目前主程式搜尋模組路徑
import sys
for place in sys.path: 
    print(place)

