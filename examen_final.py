import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from pandas.io.pytables import dropna_doc

#importar y visualizar datos

#Datos extraidos de https://sigsa.mspas.gob.gt/datos-de-salud/morbilidad/principales-causas-de-morbilidad


df = pd.read_excel("morbilidad_2019.xlsx", header=4, usecols=(2,3), nrows=21)

#imprime solo los datos a utilizar (columna 2 y 3)
print(df)

# Grafica de datos

df.plot.barh(x='Diagnóstico ', y='Total ', )
plt.title("20 Causas principales de morbilidad general año 2019")
plt.xlabel('Número de casos (millones)')
plt.ylabel('Enfermedad')
plt.show()