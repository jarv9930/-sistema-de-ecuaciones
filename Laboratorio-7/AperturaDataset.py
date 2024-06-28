import pandas as pd 
from ydata_profiling import ProfileReport

df = pd.read_csv("./bezdekIris.csv")
profile = ProfileReport(df, title="Pandas Profiling Report")
profile.to_file("./Laboratorio-7/reporte.html")
print("************************************")
print("Calculos para datos completos ")
print("_____________________________________")
for i in df.select_dtypes(include=['float64']).columns:
    print(i)
    print("Media: ", df[i].mean())
    print("Varianza: ", df[i].var())
    print("Desviación Estándar: ", df[i].std())
    print("")

print("************************************")
print("Calculos para categoria Iris-setosa")
print("_____________________________________")
for i in df[df["Categoria"] == "Iris-setosa"].select_dtypes(include=['float64']).columns:
    print(i)
    print("Media: ", df[df["Categoria"] == "Iris-setosa"][i].mean())
    print("Varianza: ", df[df["Categoria"] == "Iris-setosa"][i].var())
    print("Desviación Estándar: ", df[df["Categoria"] == "Iris-setosa"][i].std())
    print("")

print("************************************")
print("Calculos para categoria Iris-versicolor")
print("_____________________________________")
for i in df[df["Categoria"] == "Iris-versicolor"].select_dtypes(include=['float64']).columns:
    print(i)
    print("Media: ", df[df["Categoria"] == "Iris-versicolor"][i].mean())
    print("Varianza: ", df[df["Categoria"] == "Iris-versicolor"][i].var())
    print("Desviación Estándar: ", df[df["Categoria"] == "Iris-versicolor"][i].std())
    print("")

print("************************************")
print("Calculos para categoria Iris-virginica")
print("_____________________________________")
for i in df[df["Categoria"] == "Iris-virginica"].select_dtypes(include=['float64']).columns:
    print(i)
    print("Media: ", df[df["Categoria"] == "Iris-virginica"][i].mean())
    print("Varianza: ", df[df["Categoria"] == "Iris-virginica"][i].var())
    print("Desviación Estándar: ", df[df["Categoria"] == "Iris-virginica"][i].std())
    print("")
