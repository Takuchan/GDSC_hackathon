# coding: UTF-8

import topofchikin.PDF2Figure as p2f
import topofchikin.CreateGenre_noTeacher_AtsuAtsuEdition as cgn2
import topofchikin.GenerateTitle as generateTitle
import sys

def main():
    os_pdfs = sys.argv
    pdfs = p2f.PDF2Figure(os_pdfs)
    pdfs.convert()
    while (pdfs.getProcessed() == False):
        print("処置中です。")
    cgn2
    title = generateTitle.GenerateTitle().process(
    "私は、その男の写真を三葉、見たことがある。一葉は、その男の、幼年時代、とでも言うべきであろうか、十歳前後かと推定される頃の写真であって、その子供が大勢の女のひとに取りかこまれ、"
    )
    print(title)
    


if __name__ == "__main__":
    main()