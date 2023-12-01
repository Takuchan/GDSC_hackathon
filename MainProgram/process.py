import topofchikin.PDF2Figure as p2f
import topofchikin.CreateGenre_noTeacher as cgn

import sys

   

def main():
    os_pdfs = sys.argv
    pdfs = p2f.PDF2Figure(os_pdfs)
    pdfs.convert()


if __name__ == "__main__":
    main()