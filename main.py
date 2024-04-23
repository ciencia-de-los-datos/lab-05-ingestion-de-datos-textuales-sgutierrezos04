import pandas as pd
import os

carpeta_data = "./data"
test = []
train = []

for carpeta in os.listdir(carpeta_data):
    if carpeta == "__MACOSX":
        continue

    for estado in os.listdir(os.path.join(carpeta_data, carpeta)):
        if estado == ".DS_Store":
            continue

        print("\t", estado)
        for archivo in os.listdir(os.path.join(carpeta_data, carpeta, estado)):
            if archivo.endswith(".txt"):
                with open(os.path.join(carpeta_data, carpeta, estado, archivo), "r") as f:
                    frase = f.read()
                    sentimiento = estado
                    if carpeta == "test":
                        test.append((frase, sentimiento))
                    elif carpeta == "train":
                        train.append((frase, sentimiento))

test_df = pd.DataFrame(test, columns=["phrase", "sentiment"])
train_df = pd.DataFrame(train, columns=["phrase", "sentiment"])

train_df.to_csv("train_dataset.csv", index=False)
test_df.to_csv("test_dataset.csv", index=False)