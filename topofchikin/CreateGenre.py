"""
こちらは教師あり学習のを一旦開発してやめたやつです。
"""

import tensorflow as tf 
import numpy as np
from tensorflow import keras


def load_text_files(filenames,labels):
    texts = []
    for filename in filenames:
        with open(filename,encoding='utf-8',errors='ignore') as f:
            texts.append(f.read())
    return np.array(texts),np.array(labels)

def main():
    vectorize_layer = keras.layers.TextVectorization(
        max_tokens=10000,
        output_mode='int',
        output_sequence_length=200
    )