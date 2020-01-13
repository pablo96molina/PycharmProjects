import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
from sklearn import preprocessing

#Cargar los datos
df = pd.read_csv('teleCust1000t.csv')
df.head()

#Visualizacion de datos y analisis

df['custcat'].value_counts() #Cuenta cuantos de cada tipo hay

df.hist(column='income', bins=50)

#Definir features set
df.columns

#Para utilizar la librería scikit-learn, tenemos que convertir el data frame de Panda en un Numpy array
X = df[['region', 'tenure','age', 'marital', 'address', 'income', 'ed', 'employ','retire', 'gender', 'reside']] .values  #.astype(float)
X[0:5]
y = df['custcat'].values
y[0:5]

#Normalizar los datos. La estandarización de Datos brinda a los datos cero media y varianza de unidad

X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))
X[0:5]

#Train Test Split

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=4)
print ('Set de Entrenamiento:', X_train.shape,  y_train.shape)
print ('Set de Prueba:', X_test.shape,  y_test.shape)

#K Vecinos
from sklearn.neighbors import KNeighborsClassifier

#Entrenamiento, iniciar con k=4
k = 4
#Entrenar el Modelo y Predecir
neigh = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)
neigh

#Prediccion
yhat = neigh.predict(X_test)
yhat[0:5]

#Evaluacion de certezas #Accuracy score es el F1 Score
from sklearn import metrics
print("Entrenar el set de Certeza: ", metrics.accuracy_score(y_train, neigh.predict(X_train)))
print("Probar el set de Certeza: ", metrics.accuracy_score(y_test, yhat))

#Ahora con k=6
k = 6
neigh6 = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)
yhat6 = neigh6.predict(X_test)
print("Certeza del Set de Entrenamiento: ", metrics.accuracy_score(y_train, neigh6.predict(X_train)))
print("Certeza del Set de Prueba: ", metrics.accuracy_score(y_test, yhat6))

#Probar con diferentes K y encontrar el mejor

Ks = 10
mean_acc = np.zeros((Ks - 1))
std_acc = np.zeros((Ks - 1))
ConfustionMx = [];
for n in range(1, Ks):
    # Entrenar el Modelo y Predecir
    neigh = KNeighborsClassifier(n_neighbors=n).fit(X_train, y_train)
    yhat = neigh.predict(X_test)
    mean_acc[n - 1] = metrics.accuracy_score(y_test, yhat)

    std_acc[n - 1] = np.std(yhat == y_test) / np.sqrt(yhat.shape[0])

mean_acc

#Dibujo de las certezas para diferentes K
plt.plot(range(1,Ks),mean_acc,'g')
plt.fill_between(range(1,Ks),mean_acc - 1 * std_acc,mean_acc + 1 * std_acc, alpha=0.10)
plt.legend(('Certeza ', '+/- 3xstd'))
plt.ylabel('Certeza ')
plt.xlabel('Número de Vecinos (K)')
plt.tight_layout()
plt.show()

print( "La mejor aproximación de certeza fue con ", mean_acc.max(), "con k=", mean_acc.argmax()+1)