# coding: UTF-8

import topofchikin.PDF2Figure as p2f
import topofchikin.CreateGenre_noTeacher_AtsuAtsuEdition as cgn2
import topofchikin.GenerateTitle as generateTitle
import sys

def main():
    os_pdfs = sys.argv
    cluster_number = int(os_pdfs[1])
    pdfs = p2f.PDF2Figure(os_pdfs)
    pdfs.convert()
    while (pdfs.getProcessed() == False):
        print("処置中です。")
    createGeneratenoTeacher = cgn2.CreateGenre_noTeacher_AtsuAtsuEdition()
    result_list = createGeneratenoTeacher.process(cluster_num=cluster_number)
    checkedKey_dict = {}
    for key in result_list:
        print(key[0],end=' , ')
        if key[0] not in checkedKey_dict:
            sliced_text = key[1][:1000]
            title = generateTitle.GenerateTitle().process(sliced_text)
            checkedKey_dict[key[0]] = title
            print(title,end=' , ')
            print(key[2])
            print("--------------")
        else:
            print(checkedKey_dict[key[0]],end=' , ')
            print(key[2])
            print("--------------")

if __name__ == "__main__":
    main()