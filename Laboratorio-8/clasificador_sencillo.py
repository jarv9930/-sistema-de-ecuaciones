import pandas as pd 

df = pd.read_csv("./train.csv")

# Calcular la media de los valores de longitud de petalo para iris setosa
mediaSetosaL = df[df["class"] == "Iris-setosa"].iloc[:, 0].mean()
print("Media Setosa Longitud: ", mediaSetosaL)
#calcular la desviacion estandar de los valores de longitud de petalo para iris setosa
desviacionSetosaL = df[df["class"] == "Iris-setosa"].iloc[:, 0].std()
print("Desviacion Setosa Longitud: ", desviacionSetosaL)

print("------------------------------------")

# Calcular la media de los valores de longitud de petalo para iris versicolor
mediaVersicolorL = df[df["class"] == "Iris-versicolor"].iloc[:, 0].mean()
print("Media Versicolor Longitud: ", mediaVersicolorL)
#calcular la desviacion estandar de los valores de longitud de petalo para iris versicolor
desviacionVersicolorL = df[df["class"] == "Iris-versicolor"].iloc[:, 0].std()
print("Desviacion Versicolor Longitud: ", desviacionVersicolorL)


print("------------------------------------")

# Calcular la media de los valores de longitud de petalo para iris virginica
mediaVirginicaL = df[df["class"] == "Iris-virginica"].iloc[:, 0].mean()
print("Media Virginica Longitud: ", mediaVirginicaL)
#calcular la desviacion estandar de los valores de longitud de petalo para iris virginica
desviacionVirginicaL = df[df["class"] == "Iris-virginica"].iloc[:, 0].std()
print("Desviacion Virginica Longitud: ", desviacionVirginicaL)


print("************************************")

# Calcular la media de los valores de ancho de petalo para iris setosa
mediaSetosaA = df[df["class"] == "Iris-setosa"].iloc[:, 1].mean()
print("Media Setosa Ancho: ", mediaSetosaA)
#Calcular la desviacion estandar de los valores de ancho de petalo para iris setosa
desviacionSetosaA = df[df["class"] == "Iris-setosa"].iloc[:, 1].std()
print("Desviacion Setosa Ancho: ", desviacionSetosaA)

print("------------------------------------")

# Calcular la media de los valores de ancho de petalo para iris versicolor
mediaVersicolorA = df[df["class"] == "Iris-versicolor"].iloc[:, 1].mean()
print("Media Versicolor Ancho: ", mediaVersicolorA)
#Calcular la desviacion estandar de los valores de ancho de petalo para iris versicolor
desviacionVersicolorA = df[df["class"] == "Iris-versicolor"].iloc[:, 1].std()
print("Desviacion Versicolor Ancho: ", desviacionVersicolorA)

print("------------------------------------")

# Calcular la media de los valores de ancho de petalo para iris virginica
mediaVirginicaA = df[df["class"] == "Iris-virginica"].iloc[:, 1].mean()
print("Media Virginica Ancho: ", mediaVirginicaA)
#Calcular la desviacion estandar de los valores de ancho de petalo para iris virginica
desviacionVirginicaA = df[df["class"] == "Iris-virginica"].iloc[:, 1].std()
print("Desviacion Virginica Ancho: ", desviacionVirginicaA)


df2 = pd.read_csv("./test.csv")

#Clasificar los valores de archivo text considerando los resulados de la media de los valores de longitud de petalo
print("------------CLASIFICACION POR LONGITUD DE PETALO-----------------")
contIrisSetosa = 0
contIrisVersicolor = 0
contIrisVirginica = 0

contadorCorrectos = 0
for i in range(len(df2)):
    if df2.iloc[i, 0] < (mediaSetosaL + desviacionSetosaL):
        contIrisSetosa+=1
        #Comprobar si el clasificador es correcto comparando las categorias
        if df2.iloc[i, 2] == "Iris-setosa":
            contadorCorrectos+=1

    elif df2.iloc[i, 0] < (mediaVersicolorL + desviacionVersicolorL) and df2.iloc[i, 0] >  (mediaSetosaL +desviacionSetosaL):
        
        contIrisVersicolor+=1
        #Comprobar si el clasificador es correcto comparando las categorias
        if df2.iloc[i, 2] == "Iris-versicolor":
            contadorCorrectos+=1
    elif df2.iloc[i, 0] < (mediaVirginicaL + desviacionVirginicaL) and df2.iloc[i, 0] > (mediaVersicolorL + desviacionVersicolorL):
        contIrisVirginica+=1
        #Comprobar si el clasificador es correcto comparando las categorias
        if df2.iloc[i, 2] == "Iris-virginica":
            contadorCorrectos+=1


print("Cantidad de Iris-setosa: ", contIrisSetosa)
print("Cantidad de Iris-versicolor: ", contIrisVersicolor)
print("Cantidad de Iris-virginica: ", contIrisVirginica)

#Calculamos la efeciencia del clasificador dividiendo el numero de acietos con el total de muestras
accuracy = (contadorCorrectos / len(df2)) * 100

print("El clasificador acerto en ", contadorCorrectos, " muestras de ", len(df2))
print("Accuracy del clasificador por longitud de petalo: ", accuracy, "%")

#Clasificar los valores de archivo text considerando los resulados de la media de los valores de ancho de petalo
print("------------CLASIFICACION POR ANCHO DE PETALO-----------------")
contIrisSetosa = 0
contIrisVersicolor = 0
contIrisVirginica = 0

contadorCorrectos = 0
for i in range(len(df2)):
    if df2.iloc[i, 1] < (mediaSetosaA + desviacionSetosaA):
        contIrisSetosa+=1
        #Comprobar si el clasificador es correcto comparando las categorias
        if df2.iloc[i, 2] == "Iris-setosa":
            contadorCorrectos+=1

    elif df2.iloc[i, 1] < (mediaVersicolorA + desviacionVersicolorA) and df2.iloc[i, 1] > (mediaSetosaA + desviacionSetosaA):
        
        contIrisVersicolor+=1
        #Comprobar si el clasificador es correcto comparando las categorias
        if df2.iloc[i, 2] == "Iris-versicolor":
            contadorCorrectos+=1
    elif df2.iloc[i, 1] < (mediaVirginicaA + desviacionVirginicaA) and df2.iloc[i, 1] > (mediaVersicolorA + desviacionVersicolorA):
        contIrisVirginica+=1
        #Comprobar si el clasificador es correcto comparando las categorias
        if df2.iloc[i, 2] == "Iris-virginica":
            contadorCorrectos+=1
            
print("Cantidad de Iris-setosa: ", contIrisSetosa)
print("Cantidad de Iris-versicolor: ", contIrisVersicolor)
print("Cantidad de Iris-virginica: ", contIrisVirginica)

#Calculamos la efeciencia del clasificador dividiendo el numero de acietos con el total de muestras
accuracy = (contadorCorrectos / len(df2)) * 100


print("El clasificador acerto en ", contadorCorrectos, " muestras de ", len(df2))
print("Accuracy del clasificador por ancho de petalo: ", accuracy, "%")