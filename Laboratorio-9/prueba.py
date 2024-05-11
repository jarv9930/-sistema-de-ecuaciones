import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.datasets import load_iris, load_wine

def hold_out_stratified(data, target, test_size=0.3):
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=test_size, stratify=target)
    return X_train, X_test, y_train, y_test

def k_fold_stratified(data, target, n_splits=10):
    skf = StratifiedKFold(n_splits=n_splits)
    splits = skf.split(data, target)
    return splits

# Ejemplo de uso con el dataset Iris
iris = load_iris()
print("Iris data: ", iris)
X_iris, y_iris = iris.data, iris.target

X_train, X_test, y_train, y_test = hold_out_stratified(X_iris, y_iris)
splits = k_fold_stratified(X_iris, y_iris)

#Imprimir conjuntos de prueba y entrenamiento
indice = 0
print("Conjunto de entrenamiento: ")
for i in X_train:
    print(i, "->", y_train[indice])
    indice += 1
indice = 0
print("Conjunto de prueba: ")
for i in X_test:
    print(i, "->", y_test[indice])
    indice += 1

