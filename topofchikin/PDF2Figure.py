# -*- coding: utf-8 -*-
import fitz # pymupdfライブラリ
import sys
import os
from CreateGenre_noTeacher import CreateGenreNoTeacher


def main():
    pdfs = sys.argv
    get_text = ""

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
                    get_text += text
                    f.write(text)

                doc.close()
                f.close()
                
                print(f'{pdf}の処理が完了しました')
            else:
                print(f'{pdf}はPDFファイルではありません。この処理はスキップされました。')
    model = CreateGenre_noTeacher()
    model.setData(get_text)
    model.process()
    

if __name__ == '__main__':
    main()
