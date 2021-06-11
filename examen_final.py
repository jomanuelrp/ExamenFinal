import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from pandas.io.pytables import dropna_doc



df = pd.read_excel("morbilidad_2019.xlsx", header=4, usecols=(2,3), nrows=21)

print(df)

# Grafica de datos

df.plot.barh(x='Diagnóstico ', y='Total ', )
plt.title("20 Causas principales de morbilidad general año 2019")
plt.xlabel('Número de casos (millones)')
plt.ylabel('Enfermedad')
plt.show()