import numpy as np

a = np.genfromtxt('2017small-numbers.csv', delimiter=',')
print('Massimo valore dei massimi:', max(a[:,2]))
print('Numero righe e colonne:', a.shape)
print('Quarta e quinta riga: ', a[3:5])
print('Media delle chiusure: ', np.mean(a[:,0]))