import topofchikin.PDF2Figure as p2f
import topofchikin.CreateGenre_noTeacher_AtsuAtsuEdition as cgn2

import sys

def main():
    os_pdfs = sys.argv
    pdfs = p2f.PDF2Figure(os_pdfs)
    pdfs.convert()
    while (pdfs.getProcessed() == False):
        print("処置中です。")
    cgn2
    


if __name__ == "__main__":
    main()