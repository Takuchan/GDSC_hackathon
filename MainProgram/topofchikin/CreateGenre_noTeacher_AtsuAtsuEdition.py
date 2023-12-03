from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import os



class CreateGenre_noTeacher_AtsuAtsuEdition:
    def __init__(self):
        pass

    def process(self,cluster_num):
        n_clusters_input = cluster_num

        # ファイルのリストを取得します
        folder_path = 'topofchikin/datas/'  # 'your_folder'をあなたのフォルダパスに置き換えてください
        file_names = os.listdir(folder_path)
        # 各ファイルのテキストを読み込みます
        texts = []
        for file_name in file_names:
            with open(os.path.join(folder_path, file_name), 'r', encoding="utf-8") as f:
                texts.append(f.read())
        # TF-IDFベクトル化を行います
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(texts)

        # KMeansオブジェクトを作成します
        kmeans = KMeans(n_clusters=n_clusters_input)

        # モデルをトレーニングします
        kmeans.fit(X)

        # 各データポイントのクラスタラベルを取得します
        labels = kmeans.labels_
        
        text_list = [] # [[label,text,pdf名],]の順番で入っています
        # 各ファイル名と対応するラベルを出力します
        for file_name, label,text in zip(file_names, labels,texts):
            text_list.append([label,text,file_name])
            print(f"File: {file_name}, Label: {label}")
        
        return text_list