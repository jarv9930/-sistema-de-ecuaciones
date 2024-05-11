import numpy as np
import random
import pandas as pd

# Definir funciones para Hold Out 70/30 estratificado
def hold_out_70_30_stratified(X, y):
    unique_classes = np.unique(y)
    #print("Clases únicas: ", unique_classes)
    train_indices = []
    test_indices = []
    for cls in unique_classes:
        cls_indices = np.where(y == cls)[0]
        #print("Índices de la clase ", cls, ": ", cls_indices)
        np.random.shuffle(cls_indices)
        split_idx = int(0.7 * len(cls_indices))
        train_indices.extend(cls_indices[:split_idx])
        test_indices.extend(cls_indices[split_idx:])
    X_train, X_test = X[train_indices], X[test_indices]
    y_train, y_test = y[train_indices], y[test_indices]
    return X_train, X_test, y_train, y_test



# Cargar conjuntos de datos
iris = pd.read_csv("./Laboratorio-9/irisDatasets/iris.csv")


indices = list(iris.index)
random.shuffle(indices)

iris_random = iris.iloc[indices]
print("Iris random: ", iris_random)
#iris_random.to_csv("./Laboratorio-9/iris_random.csv", index=False)

# Aplicar métodos de validación en conjuntos de datos
X = iris_random.iloc[:,:-1].to_numpy()
#print("X: ", X)
y = iris_random.iloc[:, -1].values
#print("y: ", y)
iris_hold_out = hold_out_70_30_stratified(X, y)
#Imprimir conjuntos de prueba y entrenamiento
indice = 0
print("Conjunto de entrenamiento: ")
for i in iris_hold_out[0]:
    print(i, "->", iris_hold_out[2][indice])
    indice += 1
indice = 0
print("Conjunto de prueba: ")
for i in iris_hold_out[1]:
    print(i, "->", iris_hold_out[3][indice])
    indice += 1

#Guardar conjuntos de entrenamiento y prueba en archivos CSV
iris_train = pd.DataFrame(iris_hold_out[0],columns=iris.columns[:-1])
iris_train[iris.columns[-1]] = iris_hold_out[2]
iris_train.to_csv("./Laboratorio-9/irisDatasets/iris_entrenamiento.csv", index=False)
iris_test = pd.DataFrame(iris_hold_out[1],columns=iris.columns[:-1])
iris_test[iris.columns[-1]] = iris_hold_out[3]
iris_test.to_csv("./Laboratorio-9/irisDatasets/iris_prueba.csv", index=False)
