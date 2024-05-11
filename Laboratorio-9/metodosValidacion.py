import numpy as np
import pandas as pd

# Definir funciones para Hold Out 70/30 estratificado
def hold_out_70_30_estratificado(X, y):
    unique_classes = np.unique(y)
    print("Clases únicas: ", unique_classes)
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

def aplicar_hold_out_70_30_estratificado(dataset,carpeta,class_column=-1):
    
    # Aplicar métodos de validación en conjuntos de datos

    if class_column == -1:
        X = dataset.iloc[:,:-1].to_numpy()
        y = dataset.iloc[:, -1].values
    else:
        todas_las_columnas = dataset.columns
        columnas = todas_las_columnas.drop(class_column)
        X = dataset[columnas].to_numpy()
        y = dataset[class_column].values
    print("X: ", X)
    print("y: ", y)
    dataset_hold_out = hold_out_70_30_estratificado(X, y)

    #Imprimir conjuntos de prueba y entrenamiento
    indice = 0
    print("Conjunto de entrenamiento: ")
    for i in dataset_hold_out[0]:
        print(i, "->", dataset_hold_out[2][indice])
        indice += 1
    indice = 0
    print("Conjunto de prueba: ")
    for i in dataset_hold_out[1]:
        print(i, "->", dataset_hold_out[3][indice])
        indice += 1
    

    #Guardar conjuntos de entrenamiento y prueba en archivos CSV
    if class_column == -1:
        dataset_train = pd.DataFrame(dataset_hold_out[0],columns=dataset.columns[:-1])
        dataset_train[dataset.columns[-1]] = dataset_hold_out[2]
        dataset_train.to_csv(carpeta+"entrenamiento.csv", index=False)

        dataset_test = pd.DataFrame(dataset_hold_out[1],columns=dataset.columns[:-1])
        dataset_test[dataset.columns[-1]] = dataset_hold_out[3]
        dataset_test.to_csv(carpeta+"prueba.csv", index=False)
    else:
        columnas = dataset.columns.drop(class_column)
        dataset_train = pd.DataFrame(dataset_hold_out[0],columns=columnas)
        dataset_train[class_column] = dataset_hold_out[2]
        dataset_train.to_csv(carpeta+"entrenamiento.csv", index=False)

        dataset_test = pd.DataFrame(dataset_hold_out[1],columns=columnas)
        dataset_test[class_column] = dataset_hold_out[3]
        dataset_test.to_csv(carpeta+"prueba.csv", index=False)


# Cargar conjuntos de datos
iris = pd.read_csv("./Laboratorio-9/irisDatasets/iris.csv")
aplicar_hold_out_70_30_estratificado(iris,"./Laboratorio-9/irisDatasets/")

wine = pd.read_csv("./Laboratorio-9/wineDatasets/wine.csv")
aplicar_hold_out_70_30_estratificado(wine,"./Laboratorio-9/wineDatasets/","Wine")

cars = pd.read_csv("./Laboratorio-9/carsDatasets/cars.csv")
aplicar_hold_out_70_30_estratificado(cars,"./Laboratorio-9/carsDatasets/")

