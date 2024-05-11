import numpy as np
import pandas as pd
class colors:
    RESET = '\033[0m'
    BOLDRED = '\033[1;31m'
    BOLDGREEN = '\033[1;32m'
    BOLDYELLOW = '\033[1;33m'
    BOLDBLUE = '\033[1;34m'

# Funcion para Hold Out 70/30 estratificado
def hold_out_70_30_estratificado(X, y):
    #Identificar clases únicas
    unique_classes = np.unique(y)
    #print("Clases únicas: ", unique_classes)
    train_indices = []
    test_indices = []
    #Para cada clase, obtener los índices de los elementos y dividirlos en 70/30
    for cls in unique_classes:
        #Indices de la clase actual
        cls_indices = np.where(y == cls)[0]
        #print("Índices de la clase ", cls, ": ", cls_indices)
        #Mezclar los índices
        np.random.shuffle(cls_indices)
        #Dividir los índices en 70/30
        split_idx = int(0.7 * len(cls_indices))
        train_indices.extend(cls_indices[:split_idx])
        test_indices.extend(cls_indices[split_idx:])
        #Asignamos los conjuntos de entrenamiento y prueba
    X_train, X_test = X[train_indices], X[test_indices]
    y_train, y_test = y[train_indices], y[test_indices]
    return X_train, X_test, y_train, y_test

def aplicar_hold_out_70_30_estratificado(dataset,carpeta,class_column=-1):
    
    #Obtenemos los datos y las clases del dataset, si la clase no está especificada, se toma la última columna
    if class_column == -1:
        X = dataset.iloc[:,:-1].to_numpy()
        y = dataset.iloc[:, -1].values
    else:
        #Obtenemos las columnas del dataset
        todas_las_columnas = dataset.columns
        #Eliminamos la columna de la clase
        columnas = todas_las_columnas.drop(class_column)
        #Obtenemos los datos X y las clases Y del dataset
        X = dataset[columnas].to_numpy()
        y = dataset[class_column].values
    #print("X: ", X)
    #print("y: ", y)
    #Aplicamos Hold Out 70/30 estratificado
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
    #Si la clase no está especificada, se toma la última columna
    if class_column == -1:
        #Crear DataFrame con los conjuntos de entrenamiento, obteniendo las columnas del dataset original
        #Añadir la columna de datos al DataFrame
        dataset_train = pd.DataFrame(dataset_hold_out[0],columns=dataset.columns[:-1])
        #Añadir la columna de clases al DataFrame
        dataset_train[dataset.columns[-1]] = dataset_hold_out[2]
        #Guardar DataFrame de conjuntos de entrenamiento en archivo CSV
        dataset_train.to_csv(carpeta+"entrenamiento.csv", index=False)

        #Crear DataFrame con los conjuntos de prueba, obteniendo las columnas del dataset original
        #Añadir la columna de datos al DataFrame
        dataset_test = pd.DataFrame(dataset_hold_out[1],columns=dataset.columns[:-1])
        #Añadir la columna de clases al DataFrame
        dataset_test[dataset.columns[-1]] = dataset_hold_out[3]
        #Guardar DataFrame de conjuntos de prueba en archivo CSV
        dataset_test.to_csv(carpeta+"prueba.csv", index=False)
    else:
        #Si la clase está especificada, se toman todas las columnas menos la de la clase
        columnas = dataset.columns.drop(class_column)
        #Crear DataFrame con los conjuntos de entrenamiento, obteniendo las columnas del dataset original
        dataset_train = pd.DataFrame(dataset_hold_out[0],columns=columnas)
        dataset_train[class_column] = dataset_hold_out[2]
        dataset_train.to_csv(carpeta+"entrenamiento.csv", index=False)

        dataset_test = pd.DataFrame(dataset_hold_out[1],columns=columnas)
        dataset_test[class_column] = dataset_hold_out[3]
        dataset_test.to_csv(carpeta+"prueba.csv", index=False)

def k_fold_estratificado(X, y, n_folds=10):
    #Identificar clases únicas
    unique_classes = np.unique(y)
    #print("Clases únicas: ", unique_classes)
    #Crear los folds donde se almacenarán los índices de los elementos
    folds = [[] for _ in range(n_folds)]
    #Para cada clase, obtener los índices de los elementos y dividirlos en n_folds
    for cls in unique_classes:
        #Indices de la clase actual
        cls_indices = np.where(y == cls)[0]
        #Mezclar los índices
        np.random.shuffle(cls_indices)
        #print("Índices de la clase ", cls, ": ", cls_indices)
        #Dividir los índices en n_folds
        cls_split = np.array_split(cls_indices, n_folds)
        #print("Split de la clase ", cls, ": ", cls_split)
        #Asignar cada split a un fold
        for i in range(n_folds):
            folds[i].append(cls_split[i])
    
    #Imprimir los folds
    #for i in range(n_folds):
    #    print("Fold ", i, ": ", splits[i])

    return folds

def aplicar_k_fold_estratificado(dataset,carpeta,class_column=-1,n_folds=10):
        
        #Obtenemos los datos y las clases del dataset, si la clase no está especificada, se toma la última columna
        if class_column == -1:
            X = dataset.iloc[:,:-1].to_numpy()
            y = dataset.iloc[:, -1].values
        else:
            #Obtenemos las columnas del dataset
            todas_las_columnas = dataset.columns
            #Eliminamos la columna de la clase
            columnas = todas_las_columnas.drop(class_column)
            #Obtenemos los datos X y las clases Y del dataset
            X = dataset[columnas].to_numpy()
            y = dataset[class_column].values

        #Aplicamos K-Fold estratificado
        dataset_k_fold = k_fold_estratificado(X, y, n_folds)
    
        #Para cada fold, guardar los conjuntos de entrenamiento y prueba en archivos CSV
        for i in range(n_folds):
            #Obtener los índices de prueba del fold actual, empezando desde el primer fold hasta el último
            #en cada iteración, el fold i se convierte en el conjunto de prueba y los demás en el conjunto de entrenamiento
            test_indices = np.concatenate(dataset_k_fold[i])
            #print("Índices de prueba del fold ", i, ": ", test_indices)
            train_indices = []
            arregloDeArreglos = []
            #Obtener los índices de entrenamiento del fold actual, excluyendo el fold i 
            for j in range(n_folds):
                if i == j:
                    continue
                else:
                    aux = np.concatenate(dataset_k_fold[j])
                    train_indices.extend(aux)
            #print("Índices de entrenamiento del fold ", i, ": ", train_indices)
            #Asignar los conjuntos los datos y las clases de los conjuntos de entrenamiento y prueba
            X_train, X_test = X[train_indices], X[test_indices]
            y_train, y_test = y[train_indices], y[test_indices]

            #Si la clase no está especificada, se toma la última columna
            if class_column == -1:
                #Crear DataFrame con los conjuntos de entrenamiento, obteniendo las columnas del dataset original
                dataset_train = pd.DataFrame(X_train,columns=dataset.columns[:-1])
                dataset_train[dataset.columns[-1]] = y_train
                #Guardar DataFrame de conjuntos de entrenamiento en archivo CSV
                dataset_train.to_csv(carpeta+"fold_E"+str(i)+".csv", index=False)

                #Crear DataFrame con los conjuntos de prueba, obteniendo las columnas del dataset original
                dataset_test = pd.DataFrame(X_test,columns=dataset.columns[:-1])
                dataset_test[dataset.columns[-1]] = y_test
                #Guardar DataFrame de conjuntos de prueba en archivo CSV
                dataset_test.to_csv(carpeta+"fold_P"+str(i)+".csv", index=False)
                
            else:
                #Si la clase está especificada, se toman todas las columnas menos la de la clase
                columnas = dataset.columns.drop(class_column)
                #Crear DataFrame con los conjuntos de entrenamiento, obteniendo las columnas del dataset original
                dataset_train = pd.DataFrame(X_train,columns=columnas)
                dataset_train[class_column] = y_train
                #Guardar DataFrame de conjuntos de entrenamiento en archivo CSV
                dataset_train.to_csv(carpeta+"fold_E"+str(i)+".csv", index=False)

                #Crear DataFrame con los conjuntos de prueba, obteniendo las columnas del dataset original
                dataset_test = pd.DataFrame(X_test,columns=columnas)
                dataset_test[class_column] = y_test
                #Guardar DataFrame de conjuntos de prueba en archivo CSV
                dataset_test.to_csv(carpeta+"fold_P"+str(i)+".csv", index=False)


                
def comprobarProporcionalidadHoldOut(carpeta,archivoOriginal,target):
    #Cargar conjuntos de entrenamiento y prueba, y el dataset original
    original = pd.read_csv(carpeta+archivoOriginal)
    entrenamiento = pd.read_csv(carpeta+"entrenamiento.csv")
    prueba = pd.read_csv(carpeta+"prueba.csv")
    #Obtener el total de elementos en el dataset original,en el de entrenamiento y en el de prueba
    total = len(original)
    total_entrenamiento = len(entrenamiento)
    total_prueba = len(prueba)
    #Obtener cuantas clases hay en el dataset original
    clases_original = original[target].values
    #Contar cuantos elementos hay de cada clase en el dataset original
    unique_classes = np.unique(clases_original)
    for cls in unique_classes:
        print(colors.BOLDYELLOW,"----------------Clase: ", cls, "----------------",colors.RESET)
        count = np.count_nonzero(clases_original == cls)
        print("Cantidad de elementos de la clase ", cls, " en el dataset original: ", count)
        porcentaje = (count/total)*100
        print("Porcentaje de elementos de la clase ", cls, " en el dataset original: ", porcentaje, "%\n")
        #Obtener cuantas clases hay en el conjunto de entrenamiento
        clases_entrenamiento = (entrenamiento[target]==cls).sum()
        print(colors.BOLDGREEN,"Cantidad de elementos de la clase ", cls, " en el conjunto de entrenamiento: ", clases_entrenamiento)
        
        #Calcular el porcentaje de elementos de la clase actual en el conjunto de entrenamiento
        porcentaje = (clases_entrenamiento/total_entrenamiento)*100
        print("Porcentaje de elementos de la clase ", cls, " en el conjunto de entrenamiento: ", porcentaje, "%\n",colors.RESET)
        
        #Obtener cuantas clases hay en el conjunto de prueba
        clases_prueba = (prueba[target]==cls).sum()
        print(colors.BOLDBLUE,"Cantidad de elementos de la clase ", cls, " en el conjunto de prueba: ", clases_prueba)

        #Calcular el porcentaje de elementos de la clase actual en el conjunto de prueba
        porcentaje = (clases_prueba/total_prueba)*100
        print("Porcentaje de elementos de la clase ", cls, " en el conjunto de prueba: ", porcentaje, "%",colors.RESET)

def comprobarProporcionalidadKfold(carpeta,archivoOriginal,target,n_folds=10):
    #Cargar el dataset original
    original = pd.read_csv(carpeta+archivoOriginal)
    #Obtener el total de elementos en el dataset original
    total = len(original)

    #Para cada fold, comprobar la proporcionalidad de las clases
    for i in range(n_folds):
        print(colors.BOLDYELLOW,"*****************Fold: ", i, "***************",colors.RESET)
        #Cargar el fold actual
        foldEntrenamieto = pd.read_csv(carpeta+"fold_E"+str(i)+".csv")
        foldPrueba = pd.read_csv(carpeta+"fold_P"+str(i)+".csv")

        #Obtener el total de elementos de entrenamiento en el fold actual
        total_fold_entrenamiento = len(foldEntrenamieto)
        #Obtener el total de elementos de prueba en el fold actual
        total_fold_prueba = len(foldPrueba)

        #Obtener cuantas clases hay en el dataset original
        clases_original = original[target].values
        #Contar cuantos elementos hay de cada clase en el dataset original
        unique_classes = np.unique(clases_original)
        for cls in unique_classes:
            print(colors.BOLDYELLOW,"----------------Clase: ", cls, "----------------",colors.RESET)
            count = np.count_nonzero(clases_original == cls)
            print("Cantidad de elementos de la clase ", cls, " en el dataset original: ", count)
            porcentaje = (count/total)*100
            print("Porcentaje de elementos de la clase ", cls, " en el dataset original: ", porcentaje, "%\n")

            #Obtener cuantas clases hay en el conjunto de entrenamiento
            clases_entrenamiento = (foldEntrenamieto[target]==cls).sum()
            print(colors.BOLDGREEN,"Cantidad de elementos de la clase ", cls, " en el conjunto de entrenamiento: ", clases_entrenamiento)
            porcentaje = (clases_entrenamiento/total_fold_entrenamiento)*100
            print("Porcentaje de elementos de la clase ", cls, " en el conjunto de entrenamiento: ", porcentaje, "%\n",colors.RESET)

            #Obtener cuantas clases hay en el conjunto de prueba
            clases_prueba = (foldPrueba[target]==cls).sum()
            print(colors.BOLDBLUE,"Cantidad de elementos de la clase ", cls, " en el conjunto de prueba: ", clases_prueba)
            porcentaje = (clases_prueba/total_fold_prueba)*100
            print("Porcentaje de elementos de la clase ", cls, " en el conjunto de prueba: ", porcentaje, "%",colors.RESET)


def printMenu():
    print(colors.BOLDBLUE,"1. Conjunto de datos Iris Hold Out 70/30")
    print("2. Conjunto de datos Wine Hold Out 70/30")
    print("3. Conjunto de datos Cars Hold Out 70/30")
    print("4. Conjunto de datos Iris K-Fold")
    print("5. Conjunto de datos Wine K-Fold")
    print("6. Conjunto de datos Cars K-Fold",colors.RESET)    

def menu():
    # Do while para imprimir el menú
    while(True): 
        printMenu() 
        opcion = input("Seleccione una opción: ")
        if opcion == "0":
            break
        if opcion == "1":
            iris = pd.read_csv("./Laboratorio-9/irisDatasets/iris.csv")
            print(colors.BOLDRED,"//////////////////Conjunto de datos Iris Hold Out 70/30: \\\\\\\\\\\\\\\\\\\\\\",colors.RESET)
            aplicar_hold_out_70_30_estratificado(iris,"./Laboratorio-9/irisDatasets/")
            comprobarProporcionalidadHoldOut("./Laboratorio-9/irisDatasets/",archivoOriginal="iris.csv",target="variety")
        elif opcion == "2":
            wine = wine = pd.read_csv("./Laboratorio-9/wineDatasets/wine.csv")
            print(colors.BOLDRED,"//////////////////Conjunto de datos Wine Hold Out 70/30: \\\\\\\\\\\\\\\\\\\\\\",colors.RESET)
            aplicar_hold_out_70_30_estratificado(wine,"./Laboratorio-9/wineDatasets/","Wine")
            comprobarProporcionalidadHoldOut("./Laboratorio-9/wineDatasets/",archivoOriginal="wine.csv",target="Wine")
        elif opcion == "3":
            cars = pd.read_csv("./Laboratorio-9/carsDatasets/cars.csv")
            print(colors.BOLDRED,"//////////////////Conjunto de datos Cars Hold Out 70/30: \\\\\\\\\\\\\\\\\\\\\\",colors.RESET)
            aplicar_hold_out_70_30_estratificado(cars,"./Laboratorio-9/carsDatasets/")
            comprobarProporcionalidadHoldOut("./Laboratorio-9/carsDatasets/",archivoOriginal="cars.csv",target="Origin")
        elif opcion == "4":
            iris = pd.read_csv("./Laboratorio-9/irisDatasets/iris.csv")
            n_foldsL = 10
            print(colors.BOLDRED,"//////////////////Conjunto de datos Iris K-Fold: \\\\\\\\\\\\\\\\\\\\\\",colors.RESET)
            aplicar_k_fold_estratificado(iris,"./Laboratorio-9/irisDatasets/",n_folds=n_foldsL)
            comprobarProporcionalidadKfold("./Laboratorio-9/irisDatasets/",archivoOriginal="iris.csv",target="variety",n_folds=n_foldsL)
        elif opcion == "5":
            wine = wine = pd.read_csv("./Laboratorio-9/wineDatasets/wine.csv")
            n_foldsL = 10
            print(colors.BOLDRED,"//////////////////Conjunto de datos Wine K-Fold: \\\\\\\\\\\\\\\\\\\\\\",colors.RESET)
            aplicar_k_fold_estratificado(wine,"./Laboratorio-9/wineDatasets/","Wine",n_folds= n_foldsL)
            comprobarProporcionalidadKfold("./Laboratorio-9/wineDatasets/",archivoOriginal="wine.csv",target="Wine",n_folds=n_foldsL)
        elif opcion == "6":
            cars = pd.read_csv("./Laboratorio-9/carsDatasets/cars.csv")
            n_foldsL = 10
            print(colors.BOLDRED,"//////////////////Conjunto de datos Cars K-Fold: \\\\\\\\\\\\\\\\\\\\\\",colors.RESET)
            aplicar_k_fold_estratificado(cars,"./Laboratorio-9/carsDatasets/",n_folds= n_foldsL)
            comprobarProporcionalidadKfold("./Laboratorio-9/carsDatasets/",archivoOriginal="cars.csv",target="Origin",n_folds=n_foldsL)
        else:
            print("Opción no válida")
        #Presionar enter para continuar
        input("Presione Enter para continuar...")

menu()