from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import os


class TextClusterer:
    def __init__(self, n_clusters, folder_path):
        self.n_clusters = n_clusters
        self.folder_path = folder_path
        self.vectorizer = TfidfVectorizer()
        self.kmeans = KMeans(n_clusters=self.n_clusters)

    def load_texts(self):
        file_names = os.listdir(self.folder_path)
        texts = []
        for file_name in file_names:
            with open(os.path.join(self.folder_path, file_name), 'r') as f:
                texts.append(f.read())
        return file_names, texts

    def fit(self, texts):
        X = self.vectorizer.fit_transform(texts)
        self.kmeans.fit(X)
        return self.kmeans.labels_

    def print_labels(self, file_names, labels):
        for file_name, label in zip(file_names, labels):
            print(f"File: {file_name}, Label: {label}")
