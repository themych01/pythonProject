import numpy as np

# tablica = np.arange(0,4*20+1,4)
#
# print(tablica)
#zad2
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

def tablica(n):
    a = np.zeros((n*n), dtype='int32')
    for i in range(0, len(a)):
        a[i] = 2**i
    tab = a.reshape((n, n))
    return tab

print(tablica(5))