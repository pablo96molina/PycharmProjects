import numpy as np
import pandas as pd
from scipy import ndimage
from scipy.cluster import hierarchy
from scipy.spatial import distance_matrix
from matplotlib import pyplot as plt
from sklearn import manifold, datasets
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets.samples_generator import make_blobs

#Genero datos aleatorios
X1, y1 = make_blobs(n_samples=50, centers=[[4,4], [-2, -1], [1, 1], [10,4]], cluster_std=0.9)

#Clustering Aglomerativo
#n cluster es numero de clusters y centroides a generar
# linkage</b>: Criterio de Enlace a utilizar. El criterio de enlace determina la distancia a usar entre varias observaciones.
# El algoritmos agrupará en pares los clusters que minimizarán este criterio.

agglom = AgglomerativeClustering(n_clusters = 4, linkage = 'average')
agglom.fit(X1,y1)

# Crear una figura de 6 pulgadas (aprox 15cm) por 4 pulgadas (aprox 10 cm).
plt.figure(figsize=(6, 4))

# Estas dos líneas de código se usan para reducir los puntos de datos,
# porque sino los puntos de datos se verían muy separados y dispersos.

# Crear un rango mínimo y máximo de X1.
x_min, x_max = np.min(X1, axis=0), np.max(X1, axis=0)

# Obtener la distancia promedio para X1.
X1 = (X1 - x_min) / (x_max - x_min)

# Este loop muestra todos los puntos de datos.
for i in range(X1.shape[0]):
    # Reemplaza los puntos de datos con su valor de cluster respectivo
    # (ej. 0) está codificado con un mapa de colores (plt.cm.spectral)
    plt.text(X1[i, 0], X1[i, 1], str(y1[i]),
             color=plt.cm.nipy_spectral(agglom.labels_[i] / 10.),
             fontdict={'weight': 'bold', 'size': 9})

# Elimina los ticks x, ticks y, y los ejes x e y
plt.xticks([])
plt.yticks([])
# plt.axis('off')


# Muestra el punteado de los datos originales ántes de clustering
plt.scatter(X1[:, 0], X1[:, 1], marker='.')
# Muestra el punteo
plt.show()

#Matrix de distancia
dist_matrix = distance_matrix(X1,X1)
print(dist_matrix)
Z = hierarchy.linkage(dist_matrix, 'complete')#Guarda el resultado

dendro = hierarchy.dendrogram(Z)
