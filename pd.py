import numpy as np


# tablica = np.arange(0,4*20+1,4)
#
# print(tablica)
# zad2
# lista = [1.2,3.2,5.2]
#
# b = np.array(lista)
#
# print(b)
# a = b.astype('int32')
#
# print(a)
# print(a.dtype)

# zad3

# def tablica(n):
#     a = np.zeros((n*n), dtype='int32')
#     for i in range(0, len(a)):
#         a[i] = 2**i
#     tab = a.reshape((n, n))
#     return tab
#
# print(tablica(5))

# zad4
#
# def potega(x,y):
#     return np.logspace(1, y, num=y, base=x)
#
# print(potega(2,4))

# zad5

# def wektor(dlugosc):
#     a = np.arange(dlugosc, -1, -1)
#     b = np.diag(a, 2)
#     return b
#
#
# print(wektor(4))


#zad6

# malina = np.array(list('malina'))
# mrowka = np.array(list('mrówka'))
# armata = np.array(list('armata'))
# armata = np.flip(armata)
#
# print(armata)
#
# wykreslanka = np.zeros((6,6), dtype='str')
#
# print(wykreslanka)
#
# wykreslanka = np.diag(mrowka)
#
# wykreslanka[:, 0] = malina
# wykreslanka [5,:] = armata
# print(wykreslanka)
# print("")
# wykreslanka[:, 0] = mrowka
# wykreslanka[5,:: -1] = armata
# for a in range(5):
#     wykreslanka[a,a] = malina[a]
# print(wykreslanka)


