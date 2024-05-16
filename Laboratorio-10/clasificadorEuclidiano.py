import metodosValidacionIris as mvi
import pandas as pd
import numpy as np

class colors:
    RESET = '\033[0m'
    BOLDRED = '\033[1;31m'
    BOLDGREEN = '\033[1;32m'
    BOLDYELLOW = '\033[1;33m'
    BOLDBLUE = '\033[1;34m'

def metodoDeValidacion(dataset,metodo,carpeta,target,k=0):
    #print("dataset: ", dataset) 
    if metodo == 1:
        mvi.MetodosValidacion.aplicar_hold_out_70_30_estratificado(dataset,carpeta,target)
        return pd.read_csv(carpeta+"entrenamiento.csv"), pd.read_csv(carpeta+"prueba.csv")
    elif metodo == 2:
        #Leer el valor de k en entero
        mvi.MetodosValidacion.aplicar_k_fold_estratificado(dataset,carpeta,target,k)
    else:
        print("Operacion no valida")

def faseDeAprendizaje(dataset_train,target):
    ######Fase de aprendizaje######

    #Obtener las clases unicas conjunto de entrenamiento
    clases_entrenamiento = dataset_train[target].unique()
    #print("Clases de entrenamiento: ", clases_entrenamiento)
    
    #Vectores promedio
    vectores_promedio = []
    vector_clase = []

    #Obtener las columnas del conjunto de entrenamiento excepto la columna variety
    columnas = dataset_train.columns.tolist()
    columnas.remove(target)
    for cls in clases_entrenamiento:
        #Vector Auxiliar
        vector_aux = []
        #Obtener los datos de la clase actual
        datos_clase = dataset_train[dataset_train[target] == cls].drop(columns=target);
        #Calcular numero de patrones de la clase actual
        n = len(datos_clase)
        #Calcular la media para cada colmna de la clase actual
        for i in columnas:
            #print("Columna: ", i)
            media = datos_clase[i].mean()
            vector_aux.append(media)

        print(colors.BOLDBLUE,"Vector promedio para la clase ", cls, ": ", vector_aux, colors.RESET)
        vectores_promedio.append(vector_aux)
        #Asignar clase al vector promedio
        vector_clase.append(cls)

    #print("Vector clase: ", vector_clase)
    #print("Vectores promedio: ", vectores_promedio)
    return vectores_promedio, vector_clase

def distanciaEuclidiana(patron,vector_promedio):
    if len(patron) != len(vector_promedio):
        print("Los vectores no tienen la misma longitud")
        return None
    sumaDeCuadrados = 0
    for i in range(len(patron)):
        sumaDeCuadrados += (patron[i] - vector_promedio[i])**2
    return np.sqrt(sumaDeCuadrados)


def faseDeClasificacion(dataset_test,vectores_promedio,target,vector_clase):
    ######Fase de clasificacion######
    #Calcular la distancia euclidiana entre cada patron de prueba y los vectores promedio
    total_aciertos = 0
    columnas = dataset_test.columns.tolist()
    for i in range(len(dataset_test)):
        print(  colors.BOLDYELLOW,"-------------Patron ", i+1, "-------------", colors.RESET)
        #Obtener el patron de prueba
        patron = dataset_test.iloc[i].drop(target).values
        print("Patron Actual: ", patron)
        #Calcular la distancia entre el patron y los vectores promedio
        distancias = []
        j = 0
        for vector in vectores_promedio:
            #Obtener el nombre de la clase
            clase = vector_clase[j]
            #obtener la distancia euclidiana
            distancia = distanciaEuclidiana(patron,vector)
            print(colors.BOLDGREEN,"Distancia de la clase ",clase,":", distancia)
            distancias.append(distancia)
            j += 1
        #print("Distancias: ", distancias)

        #Obtener la clase con la menor distancia
        indice_clase = distancias.index(min(distancias))
        clase_predicha = vector_clase[indice_clase]
        print(colors.BOLDBLUE,"Clase predicha: ", clase_predicha, colors.RESET)
        #Comprobar si la clase predicha es correcta
        if clase_predicha == dataset_test.iloc[i][target]:
            total_aciertos += 1

    print(colors.BOLDRED,"Total de aciertos: ", total_aciertos, " de ", len(dataset_test), colors.RESET)
    #Calcular la eficiencia del clasificador
    eficiencia = total_aciertos/len(dataset_test)
    #print("Eficiencia del clasificador: ", eficiencia)
    return eficiencia
    

def clasificadorEuclidianoHoldOut(dataset,carpeta,target):
    #Eliminar las columnas que no sean numeros flotantes o entero, manteniendo la columna target
    columnas = dataset.columns.tolist()
    columnas.remove(target)
    for columna in columnas:
        if dataset[columna].dtype == "object":
            dataset = dataset.drop(columns=columna)

    #Imprimir el datase
    #print("Dataset: ", dataset)

    dataset_train,dataset_test = metodoDeValidacion(dataset,1,carpeta,target,0)

    #print("Dataset de entrenamiento: ", dataset_train)
    #print("Dataset de prueba: ", dataset_test)
    vectores_promedio,vector_clase = faseDeAprendizaje(dataset_train,target)
    eficiencia = faseDeClasificacion(dataset_test,vectores_promedio,target,vector_clase)
    print("Eficiencia del clasificador: ", eficiencia)
    
def clasificadorEuclidianoKFold(dataset,carpeta,target, k):
    #Eliminar las columnas que no sean numeros flotantes o entero, manteniendo la columna target
    columnas = dataset.columns.tolist()
    columnas.remove(target)
    for columna in columnas:
        if dataset[columna].dtype == "object":
            dataset = dataset.drop(columns=columna)
    
    metodoDeValidacion(dataset,2,carpeta,target,k)

    #Realizar la validacion con cada fold y calcular la media de la eficiencia
    eficiencias = []
    for i in range(k):
        print("-------------Fold ", i+1, "-------------")
        dataset_train = pd.read_csv(carpeta+"fold_E"+str(i)+".csv")
        dataset_test = pd.read_csv(carpeta+"fold_P"+str(i)+".csv")
        vectores_promedio,vector_clase = faseDeAprendizaje(dataset_train,target)
        eficiencia = faseDeClasificacion(dataset_test,vectores_promedio,target,vector_clase)
        eficiencias.append(eficiencia)
        print("Eficiencia del fold ", i+1, ": ", eficiencia)
    eficiencia_media = np.mean(eficiencias)
    print(colors.BOLDRED,"Eficiencia media: ", eficiencia_media, colors.RESET)


def menu_dataset():
    print("1. Iris")
    print("2. Cars")
    print("3. Wine")
    print("4. Salir")
    opcion = int(input("Seleccione un dataset: "))
    return opcion

def menuClasificador():
    print("1. Clasificador Euclidiano Hold-Out")
    print("2. Clasificador Euclidiano K-Fold")
    print("3. Salir")
    opc = int(input("Seleccione una opcion: "))
    return opc

def menu():
    opcion = 0
    while opcion != 4:
        opcion = menu_dataset()
        if opcion == 1:
            dataset = pd.read_csv("./irisDataset/iris.csv") 
            target = "variety"
            carpeta = "./irisDataset/"
            
        elif opcion == 2:
            dataset = pd.read_csv("./carsDataset/cars.csv")
            target = "Origin"
            carpeta = "./carsDataset/"
            
        elif opcion == 3:
            dataset = pd.read_csv("./wineDataset/wine.csv")
            target = "Wine"
            carpeta = "./wineDataset/"

        elif opcion == 4:    
            break
        opcion_clasificador = 0
        while opcion_clasificador != 3:
            print("********************************************")
            opcion_clasificador = menuClasificador()
            if opcion_clasificador == 1:
                clasificadorEuclidianoHoldOut(dataset,carpeta,target)
            elif opcion_clasificador == 2:
                k = int(input("Ingrese el valor de k: "))
                clasificadorEuclidianoKFold(dataset,carpeta,target,k)
            elif opcion_clasificador == 3:
                break
    
menu()
