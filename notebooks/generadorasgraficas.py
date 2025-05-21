import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dataframe_asistencia = pd.read_csv("./data/asistencia_estudiantes_completo.csv")

#GRAFICANDO
"""
Gráfica de barras
"""

colors = ["#389f5c", "#00906e", "#007f78", "#006c77", "#185a6c", "#2f4858"]

plt.figure(figsize = (8, 5))

sns.countplot(x = 'estado', data = dataframe_asistencia, palette = colors)

plt.title("Cantidad de registros por estado")

plt.xlabel("Estado de asistencia")

plt.ylabel("Cantidad de registros")

plt.tight_layout()

plt.show()

"""
Gráfica de tortas
-Mostrar proporciones entre dos columnas del Df 
(proporcion de estudiantes x medio de transporte)
"""

conteo_medio_transporte = dataframe_asistencia['medio_transporte'].value_counts()

plt.figure(figsize = (5, 5))

plt.pie(
    conteo_medio_transporte,
    labels = conteo_medio_transporte.index,
    autopct='%1.1f%%',
    colors = sns.color_palette("Blues")

)

plt.title("Distribución de estudiantes por medio de transporte")

plt.tight_layout()

plt.show()

"""
Gráfico de barras agrupadas
se aplica cuando hice cruces en el dataframe
"""

conteo_estado_medio_transporte = dataframe_asistencia.groupby(['estado', 'medio_transporte']).size().unstack(fill_value = 0)

conteo_estado_medio_transporte.plot(
    kind = 'bar',
    figsize = (10, 6),
    color = colors

)

plt.title("Registros por estado de asistencia y medio de transporte")

plt.xlabel("Estado de asistencia")

plt.ylabel("Cantidad de registros")

plt.legend(title = "Medio de transporte")

plt.tight_layout()

plt.show()
    

