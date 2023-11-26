import tkinter as tk
from tkinter import filedialog

class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("sazameki Mover")
        master.geometry("400x200")

        self.file_label = tk.Label(master, text="選択したファイル: ")
        self.file_label.pack()

        self.select_button = tk.Button(master, text="ファイルを選択", command=self.select_file)
        self.select_button.pack()

        self.complete_button = tk.Button(master, text="完了", command=self.show_selected_file)
        self.complete_button.pack()

        self.classify_button = tk.Button(master, text="分類", command=self.run_classification)
        self.classify_button.pack()

    def select_file(self):
        file_path = filedialog.askopenfilename()
        # 選択したファイルに対する処理をここに追加
        self.selected_file = file_path

    def show_selected_file(self):
        try:
            file_name = self.selected_file
            self.file_label.config(text=f"選択したファイル: {file_name}")
        except AttributeError:
            self.file_label.config(text="ファイルが選択されていません")

    def run_classification(self):
        try:
            # 分類に関するPythonコードをここに追加
            print(f"分類ボタンが押されました。選択したファイル: {self.selected_file}")
        except AttributeError:
            print("ファイルが選択されていません")

if __name__ == "__main__":
    root = tk.Tk()
    my_gui = MyGUI(root)
    root.mainloop()
