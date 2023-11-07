#選資料夾
import tkinter as tk
import os
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def selcet_file():
    file_path = filedialog.askdirectory()
    print(file_path)
    return file_path
    #存放目標資料夾
    if not os.path.exists('file_path'):
        return print('已有此檔案夾請再確認')
        
        
def selcet_doc():
    doc_path = filedialog.askopenfilename(filetypes = (("csv files","*.csv"),("all files","*.*")))
    print(doc_path)
    return doc_path
