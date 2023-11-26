from tkinter import *

root = Tk()
root.title("sazameki Mover")

# ラベル設定
choseLabel = Label(root, text="ファイルを選択してください。")

# ボタン設定
button1 = Button(root, text="ファイル選択", command={})
button2 = Button(root, text="分類開始", command={})

# 配置
choseLabel.pack()
button1.pack()
button2.pack()

root.mainloop()