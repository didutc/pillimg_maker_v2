import tkinter
from tkinter import filedialog
import os
import re
initial_dir = os.getcwd()
root = tkinter.Tk()
root.withdraw()
fileselct = filedialog.askdirectory(initialdir=initial_dir)
print(fileselct)
# 현재 디렉토리 내의 모든 파일에 대해 작업
for filename in os.listdir(fileselct):
    filename_dot = filename.split('.')[0]
    # 파일명에 "-"가 있고, 그 전 문자열이 알파벳인 경우
    filename_splt=filename_dot.split('-')[0]
    if len(filename_splt) > 6:
        filename_ch = filename[0]+'h'+filename[1:]
        os.rename(fileselct+'/'+filename, fileselct+'/'+filename_ch)
