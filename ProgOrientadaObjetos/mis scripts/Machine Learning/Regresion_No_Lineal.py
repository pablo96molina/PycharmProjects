import numpy as np
import matplotlib.pyplot as plt
# Eligiendo un modelo
# A primera vista, determinamos que la función lógica podría ser una buena primera aproximación, ya que tiene
# la propiedad de comenzar con un crecimiento leve, aumentando en el medio y luego descendiendo nuevamente hacia el final; como se ve debajo:

X = np.arange(-5.0, 5.0, 0.1)
Y = 1.0 / (1.0 + np.exp(-X))

plt.plot(X,Y)
plt.ylabel('Variable Dependiente')
plt.xlabel('Variable Independiente')
plt.show()

def sigmoid(x, Beta_1, Beta_2):
    y = 1 / (1 + np.exp(-Beta_1 * (x - Beta_2)))
    return y

beta_1 = 0.10
beta_2 = 1990.0

#función logística
Y_pred = sigmoid(x_data, beta_1 , beta_2)

#predicción de puntos
plt.plot(x_data, Y_pred*15000000000000.)
plt.plot(x_data, y_data, 'ro')

# Normalicemos nuestros datos
xdata =x_data/max(x_data)
ydata =y_data/max(y_data)