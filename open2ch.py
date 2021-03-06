# coding: UTF-8
import requests
import os
from bs4 import BeautifulSoup

# tkinterモジュールのインポート
import sys
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

path = 'output.html'

def Makehtml(url):

# if __name__ == '__main__':
#     url = "\
# https://hayabusa.open2ch.net/test/read.cgi/livejupiter/1622292091/\
# "
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser') # BeautifulSoupの初期化
   
    #title 抽出
    f = open(path, 'w', encoding='UTF-8')
    title = soup.find("title")      
    f.write(title.get_text())       #textにしてファイル出力

    clas = soup.find_all('dt')
    # print(soup)
    # print(clas)
    for ii in clas:
        for i in soup.find_all("a"):
            if i.find("href"):
                del i.attrs["href"]
        # print(ii)
        f.write(str(ii))
        f.write("<br><br>\n")
     
    f.close()

 

#
# ボタンが押されるとここが呼び出される
#


def UI():
    # テキスト処理
    def click_export_button():
        url = EditBox.get()
        Makehtml(url)
        f = open(path, encoding="utf-8")
        textBox.delete(0.0,tkinter.END)
        text_data = f.read()
        textBox.insert(END, text_data)

    def click_delete_button():
        EditBox.delete(0,tkinter.END)
    def click_copy_button():
        f = open(path, encoding="utf-8")
        text_data = f.read()
        root.clipboard_append(text_data)
    
    # tkinter  
    root = tkinter.Tk()
    root.title("Open2ch scraping")
    root.geometry("400x300")

   # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # 「ファイル」ラベルの作成
    s = StringVar()
    s.set('URL：')
    label1 = ttk.Label(frame1, textvariable=s)
    label1.grid(row=0, column=0)

    # 参照ファイルのパスを表示するテキストボックスの作成
    EditBox = StringVar()
    EditBox = tkinter.Entry(frame1,width=30)
    EditBox.insert(tkinter.END,"")
    EditBox.grid(row=0, column=1)

    # URL 削除ボタン
    button = ttk.Button(frame1, text='delete URL', command=click_delete_button, width=10)
    button.grid(row=1, column=1)

    # Frame2の作成
    frame2 = ttk.Frame(root, padding=10)
    frame2.grid()
    
    # テキスト出力ボタンの作成
    export_button = ttk.Button(frame2, text='ファイルの中身を出力', command=click_export_button, width=20)
    export_button.grid(row=0, column=0)

    # コピーボタンの作成
    copy_button = ttk.Button(frame2, text='全選択コピー', command=click_copy_button, width=20)
    copy_button.grid(row=1, column=0)


    # テキスト出力ボックスの作成
    textboxname = StringVar()
    textboxname.set('\n\n出力内容 ')
    label3 = ttk.Label(frame2, textvariable=textboxname)
    label3.grid(row=2, column=0)
    textBox = Text(frame2, width=50)
    textBox.grid(row=3, column=0)

    root.mainloop()



# 
# main関数
# 

if __name__ == '__main__':
    UI()







# 参考 【保存版】Pythonでスクレイピングする方法を初心者向けに徹底解説！【サンプルコードあり】
# https://dividable.net/programming/python/python-scraping

