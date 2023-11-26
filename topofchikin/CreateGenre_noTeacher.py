from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np



# 別クラスから呼び出される
class CreateGenreNoTeacher:

    def setData(self,data):
        self.data = data
        self.process()

    def process(self):
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(self.data)
        kmeans = KMeans(n_clusters=3)
        kmeans.fit(self.data)

        predictions = kmeans.predict(X)
        texts = "あほぼけかす"
        for text,cluster in zip(texts,predictions):
            if cluster == 0:
                print(f'Text: {text} belongs to cluster 0')
                
        
