import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_excel(r'C:\Users\santi\OneDrive - Universidad de los Andes\3er Semestre\Metodos Computacionales\Taller 1 - datos ejercicio 2.0.2.xlsx')

max = [False]*198

for indice, fila in datos.iterrows():
    if indice == len(datos)-1:
        if datos.at[indice-1, "y"] < fila["y"]:
            max[indice] = True
    else:
        if datos.at[indice+1, "y"] < fila["y"] and datos.at[indice-1, "y"] < fila["y"]:
            max[indice] = True
            
datos["max"] = max

for i in range(len(datos)):
    if datos.at[i,"max"]:
        plt.scatter(datos.at[i,"x"], datos.at[i,"y"], c = "red")

plt.plot(datos["x"], datos["y"])
plt.title('Máximos Locales', fontsize=12)
plt.xlabel('x', fontsize=8)
plt.ylabel('y', fontsize=8)
plt.show()