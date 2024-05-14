import metodosValidacionIris as mvi
import pandas as pd
import numpy as np

#Cargar el dataset de Iris
dataset = pd.read_csv("./irisDataset/iris.csv")

#Aplicar Hold out 70/30 estratificado al dataset de Iris
mvi.MetodosValidacion.aplicar_hold_out_70_30_estratificado(dataset,"./irisDataset/")


#Fase de aprendizaje
#Cargar el conjunto de entrenamiento
dataset_train = pd.read_csv("./irisDataset/entrenamiento.csv ")
#Obtener las clases unicas conjunto de entrenamiento
clases_entrenamiento = dataset_train["variety"].unique()
print("Clases de entrenamiento: ", clases_entrenamiento)
#Obtener los datos del conjunto de entrenamiento
X_train = dataset_train.drop(columns="variety").values
#print("Datos de entrenamiento: ", X_train)

for cls in clases_entrenamiento:
    #Obtener los datos de la clase actual
    datos_clase = dataset_train[dataset_train["variety"] == cls].drop(columns="variety").values
    #Calcular numero de patrones de la clase actual
    n = len(datos_clase)
    sumatoria = 0  
        

#Se calculara la media por cada columna de nuestro conjunto de entrenamiento,
# el vector promedio sera un vector de 4