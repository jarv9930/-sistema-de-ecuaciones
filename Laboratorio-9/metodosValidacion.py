import numpy as np
import pandas as pd

# Definir funciones para Hold Out 70/30 estratificado
def hold_out_70_30_estratificado(X, y):
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
    #print("X: ", X)
    #print("y: ", y)
    dataset_hold_out = hold_out_70_30_estratificado(X, y)

    #Imprimir conjuntos de prueba y entrenamiento
    #indice = 0
    #print("Conjunto de entrenamiento: ")
    #for i in dataset_hold_out[0]:
    #    print(i, "->", dataset_hold_out[2][indice])
    #    indice += 1
    #indice = 0
    #print("Conjunto de prueba: ")
    #for i in dataset_hold_out[1]:
    #    print(i, "->", dataset_hold_out[3][indice])
    #    indice += 1
    

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

def k_fold_estratificado(X, y, n_splits=10):
    unique_classes = np.unique(y)
    #print("Clases únicas: ", unique_classes)
    splits = [[] for _ in range(n_splits)]
    for cls in unique_classes:
        cls_indices = np.where(y == cls)[0]
        np.random.shuffle(cls_indices)
        #print("Índices de la clase ", cls, ": ", cls_indices)
        cls_split = np.array_split(cls_indices, n_splits)
        #print("Split de la clase ", cls, ": ", cls_split)
        for i in range(n_splits):
            splits[i].append(cls_split[i])
    
    #Imprimir los folds
    #for i in range(n_splits):
    #    print("Fold ", i, ": ", splits[i])

    return splits

def aplicar_k_fold_estratificado(dataset,carpeta,class_column=-1,n_splits=10):
        
        # Aplicar métodos de validación en conjuntos de datos
        if class_column == -1:
            X = dataset.iloc[:,:-1].to_numpy()
            y = dataset.iloc[:, -1].values
        else:
            todas_las_columnas = dataset.columns
            columnas = todas_las_columnas.drop(class_column)
            X = dataset[columnas].to_numpy()
            y = dataset[class_column].values

        dataset_k_fold = k_fold_estratificado(X, y, n_splits)
    
        #Guardar conjuntos de entrenamiento y prueba en archivos CSV
        for i in range(n_splits):
            test_indices = np.concatenate(dataset_k_fold[i])
            #print("Índices de prueba del fold ", i, ": ", test_indices)
            train_indices = []
            arregloDeArreglos = []
            for j in range(n_splits):
                if i == j:
                    continue
                else:
                    aux = np.concatenate(dataset_k_fold[j])
                    train_indices.extend(aux)
            #print("Índices de entrenamiento del fold ", i, ": ", train_indices)
            X_train, X_test = X[train_indices], X[test_indices]
            y_train, y_test = y[train_indices], y[test_indices]

            if class_column == -1:
                dataset_train = pd.DataFrame(X_train,columns=dataset.columns[:-1])
                dataset_train[dataset.columns[-1]] = y_train
                dataset_train.to_csv(carpeta+"fold_"+str(i)+".csv", index=False)

                with open(carpeta+"fold_"+str(i)+".csv", 'a') as f:
                    f.write("Conjuntos de prueba\n")
                    dataset_test = pd.DataFrame(X_test,columns=dataset.columns[:-1])
                    dataset_test[dataset.columns[-1]] = y_test
                    dataset_test.to_csv(f, index=False,lineterminator='\n')
                
            else:
                columnas = dataset.columns.drop(class_column)
                dataset_train = pd.DataFrame(X_train,columns=columnas)
                dataset_train[class_column] = y_train
                dataset_train.to_csv(carpeta+"fold_"+str(i)+".csv", index=False)

                with open(carpeta+"fold_"+str(i)+".csv", 'a') as f:
                    f.write("Conjuntos de prueba\n")
                    dataset_test = pd.DataFrame(X_test,columns=columnas)
                    dataset_test[class_column] = y_test
                    dataset_test.to_csv(f, index=False,lineterminator='\n')


                
       


# Cargar conjuntos de datos
iris = pd.read_csv("./Laboratorio-9/irisDatasets/iris.csv")
wine = pd.read_csv("./Laboratorio-9/wineDatasets/wine.csv")
cars = pd.read_csv("./Laboratorio-9/carsDatasets/cars.csv")

aplicar_hold_out_70_30_estratificado(iris,"./Laboratorio-9/irisDatasets/")
aplicar_hold_out_70_30_estratificado(wine,"./Laboratorio-9/wineDatasets/","Wine")
aplicar_hold_out_70_30_estratificado(cars,"./Laboratorio-9/carsDatasets/")

aplicar_k_fold_estratificado(iris,"./Laboratorio-9/irisDatasets/",n_splits=10)
aplicar_k_fold_estratificado(wine,"./Laboratorio-9/wineDatasets/",class_column="Wine",n_splits=10)
aplicar_k_fold_estratificado(cars,"./Laboratorio-9/carsDatasets/",n_splits=10)


