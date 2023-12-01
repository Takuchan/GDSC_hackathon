# -*- coding: utf-8 -*-
import fitz # pymupdfライブラリ
import sys
import os

class PDF2Figure:
    def __init__(self, pdfs):
        self.pdfs = pdfs
        self.texts = []

    def convert(self):
        if len(self.pdfs) == 1:
            print('引数にPDFファイルを指定してください')
        else:
            for pdf in self.pdfs[1:]:
                if pdf.endswith('.pdf'):
                    doc = fitz.open(pdf)
                    for page in range(len(doc)):
                        tmp = doc[page].get_text()
                        tmp2 = tmp.encode('utf-8','ignore')
                        text = tmp2.decode('utf-8')
                        self.texts.append([text])

                    doc.close()
                    print(f'{pdf}の処理が完了しました')
                else:
                    print(f'{pdf}はPDFファイルではありません。この処理はスキップされました。')
    def getProcessedTexts(self):
        return self.texts
    
def main():
    pdfs = sys.argv
    pdf2figure = PDF2Figure(pdfs)
    pdf2figure.convert()

if __name__ == "__main__":
    main()
