import pandas as pd 
from ydata_profiling import ProfileReport

df = pd.read_csv("./Laboratorio-8/train.csv")

# Calcular la media de los valores de longitud de petalo para iris setosa
mediaSetosaL = df[df["class"] == "Iris-setosa"].iloc[:, 0].mean()
print("Media Setosa Longitud: ", mediaSetosaL)

# Calcular la media de los valores de longitud de petalo para iris versicolor
mediaVersicolorL = df[df["class"] == "Iris-versicolor"].iloc[:, 0].mean()
print("Media Versicolor Longitud: ", mediaVersicolorL)

# Calcular la media de los valores de longitud de petalo para iris virginica
mediaVirginicaL = df[df["class"] == "Iris-virginica"].iloc[:, 0].mean()
print("Media Virginica Longitud: ", mediaVirginicaL)

print("************************************")

# Calcular la media de los valores de ancho de petalo para iris setosa
mediaSetosaA = df[df["class"] == "Iris-setosa"].iloc[:, 1].mean()
print("Media Setosa Ancho: ", mediaSetosaA)

# Calcular la media de los valores de ancho de petalo para iris versicolor
mediaVersicolorA = df[df["class"] == "Iris-versicolor"].iloc[:, 1].mean()
print("Media Versicolor Ancho: ", mediaVersicolorA)

# Calcular la media de los valores de ancho de petalo para iris virginica
mediaVirginicaA = df[df["class"] == "Iris-virginica"].iloc[:, 1].mean()
print("Media Virginica Ancho: ", mediaVirginicaA)


df2 = pd.read_csv("./Laboratorio-8/test.csv")

#Clasificar los valores de archivo text considerando los resulados de la media
contIrisSetosa = 0
contIrisVersicolor = 0
contIrisVirginica = 0

contadorCorrectos = 0
for i in range(len(df2)):
    if df2.iloc[i, 0] < mediaSetosaL:
        print("Iris-setosa")
        contIrisSetosa+=1
        #Comprobar si el clasificador es correcto comparando las categorias
        if df2.iloc[i, 2] == "Iris-setosa":
            print("Clasificación correcta")
            contadorCorrectos+=1

    elif df2.iloc[i, 0] < mediaVersicolorL and df2.iloc[i, 0] > mediaSetosaL:
        print("Iris-versicolor")
        contIrisVersicolor+=1
        #Comprobar si el clasificador es correcto comparando las categorias
        if df2.iloc[i, 2] == "Iris-versicolor":
            print("Clasificación correcta")
            contadorCorrectos+=1
    else:
        print("Iris-virginica")
        contIrisVirginica+=1
        #Comprobar si el clasificador es correcto comparando las categorias
        if df2.iloc[i, 2] == "Iris-virginica":
            print("Clasificación correcta")
            contadorCorrectos+=1

print("************************************")
print("Cantidad de Iris-setosa: ", contIrisSetosa)
print("Cantidad de Iris-versicolor: ", contIrisVersicolor)
print("Cantidad de Iris-virginica: ", contIrisVirginica)

#Calculamos la efeciencia del clasificador dividiendo el numero de acietos con el total de muestras
eficiencia = contadorCorrectos / len(df2)
print("Eficiencia del clasificador: ", eficiencia)