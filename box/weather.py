'''模組與套件說明
模組名稱就是一個檔案名稱
套件名稱是資料夾名稱
*from 模組名稱 import 方法名稱
*from 下層資料夾名稱 import 模組名稱
 (主程式要在同個資料夾裡)
'''
#主程式: boxes/weather.py.

from sources import daily, weekly
print("Daily forecast:", daily.forecast()) 
print("Weekly forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
	print(number, outlook)