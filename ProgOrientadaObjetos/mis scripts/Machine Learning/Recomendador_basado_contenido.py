#Librería de manipulación del marco de datos
import pandas as pd
#Funciones matemáticas, necesitaremos la función sqrt para importar sólo lo necesario
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

#Guardando la información de las películas dentro del marco de datos pandas
movies_df = pd.read_csv('movies.csv')
#Guardando la información del usuario dentro del marco de datos pandas
ratings_df = pd.read_csv('ratings.csv')
#Head es una función que obtiene los primeros N registros de un marco de datos. El valor por omision de N es 5.
movies_df.head()