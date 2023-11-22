# -*- coding: utf-8 -*-
import fitz # pymupdfライブラリ

pdf = 'main.pdf'
doc = fitz.open(pdf)

file = f'{pdf}_to_text.txt'
f = open(file, 'w',  encoding='utf-8', errors='ignore')

for page in range(len(doc)):
    tmp = doc[page].get_text()
    tmp2 = tmp.encode('utf-8','ignore')
    text = tmp2.decode('utf-8')
    f.write(text)

doc.close()
f.close() 