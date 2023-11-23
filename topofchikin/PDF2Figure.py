# -*- coding: utf-8 -*-
import fitz # pymupdfライブラリ
import sys
import os


def main():
    pdfs = sys.argv

    
    if len(pdfs) == 1:
        print('引数にPDFファイルを指定してください')
    else:
        for pdf in pdfs[1:]:
            if pdf.endswith('.pdf'):
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
                print(f'{pdf}の処理が完了しました')
            else:
                print(f'{pdf}はPDFファイルではありません。この処理はスキップされました。')
        

if __name__ == '__main__':
    main()
