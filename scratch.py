import numpy as np
#
# # inicjujemy dane
#
# a = np.array([20,30,40,50])
# b = np.arange(4)
#
# print(a)
# print(b)
#
# # wykonujemy operację i zapisujemy do nowej zmiennej
#
# c = a - b
# print(c)
#
# # wykonujemy operację: kwadrat zawartości
#
# print(b**2)
#
# # możemy również modyfikować obecne dane
#
# print(a)
#
# a += b
# print(a)
#
# a-=b
# print(a)

#
# a = np.arange(12).reshape((3,4))
# print(a)
# # suma całej macierzy
#
# print(a.sum())
#
# # suma każdej z kolumn
#
# print(a.sum(axis=0))
#
# # minimum każdego rzędu
#
# print(a.min(axis=1))
#
# # skumulowana suma dla rzędu
# print(a.cumsum(axis=1))
#
#inicjujemy dane

# a = np.arange(3)
# b = np.arange(3)
#
# print(a)
# print(b)
# print(a.dot(b)) # iloczyn macierzy
# print(np.dot(a,b)) # inny sposób


# a =np.ones(3, dtype='int32')
# print(a.dtype)
# # macierz zmiennoprzecinkowa
# b = np.linspace(0,np.pi,3)
# print(b.dtype)
#
# # wynikiem jest macierz zmiennoprzecinkowa
#
# c = a+b
#
# print(c)
# print(c.dtype)
#
# #wynikiem jest macierz liczb zespolonych
#
# d = np.exp(c*1j)
#
# print(d)
# print(d.dtype)
# #
# # Funkcje uniwersalne

# b = np.arange(3)
# print(b)
# print(np.exp(b))
# print(np.sqrt(b))
# c= np.array([2.,-1.,4.])
# print(np.add(b,c))

# Iteracja tablic

# Tablice wielowymiarowe iterujemy w odniesieniu do pierwszej osi!

#przykład

# # generujemy macierz 3x2
# a = np.arange(6).reshape((3,2))
# print(a)
#
# for b in a:
#     # iterujemy wśród pierwszej osi
#     print(b)
#     print("")

##### Możemy również iterować wszystkie elementy macierzy jakby była macierzą PŁASKĄ

## generujemy macierz 3x2

# a = np.arange(6).reshape((3,2))
#
# print(a)
# for b in a.flat:
#     #iterujemy jakby była to macierz płaska
#     print(b)
#     print("")

#### Przekształcenia -

## kształt tablicy jest okreslany po ilości wymiarów na każdej z osi

# a = np.arange(6)
# print(a)
# print(a.shape)
#
# # generujemy macierz 3x3
#
# b = np.array([np.arange(3),np.arange(3),np.arange(3)])
# print(b)
# print(b.shape)
#
# #generujemy macierz 1x6
# a = np.arange(6)
# print(a)
# print(a.shape)
# print("")
# #przekształcamy ją na macierz 2x3
# b = a.reshape((2,3))
# print(b)
# print(b.shape)
# print("")
# #przekształcamy ją na macierz 3x2
# c = b.reshape((3,2))
# print(c)
# print(c.shape)
# print("")
#
# #spłaszczamy macierz zyskując pierwotny kształt ze zmiennej a
#
# d = c.ravel()
# print(d)
# print(d.shape)
# print("")
#
# #transpozycja macierzy
# e = b.T
# print(b)
# print(e)
# print(e.shape)

#zad 1 Utwórz dwie macierze 1x3 różnych wartości a następnie wykonaj operację mnożenia.

# a = np.full((1,3),5)
# b = np.full((1,3),2)
# print(a)
# print(a.shape)
# print(b)

# c= a*b
# print(c)

# #zad 2 Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.
#
# a = np.array([(1,2,3),(4,5,6)])
# b = np.array([(7,8,9,10),(11,12,13,14)])
# print(a)
# print(b)
#
# print(np.min(a,axis=0))
# print(np.min(a,axis=1))
# print(np.min(b,axis=0))
# print(np.min(b,axis=1))

# ZAD3 Wykorzystaj macierze z zadania pierwszego i wykonaj iloczyn macierzy.


# c = np.dot(a,b.ravel())
# print(c)

#zad 4 Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite, a druga
# liczby rzeczywiste. Następnie wykonaj na nich operację mnożenia.


# a4 = np.array([1,2,3])
# b4 = np.linspace(3,10,3)
# print(a4)
# print(b4)
#
# print(a4*b4)

# zad 5 Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości i
# zapisz do zmiennej “a”.


# a5 = np.array([[2,7],[19,1],[10,13]])
# print(a5)
# a = np.sin(a5)
#
# print(a)
#
# a6 = np.array([[1,2],[8,5],[4,11]])
# b = np.cos(a6)
#
# print(b)
#
# c = a + b
# print(c)
#
# print(np.add(a,b))

# ZAD 8 Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.


# a8 = np.array([[1,1,1],[2,2,2],[3,3,3]])
# print(a8)
# b = 0
# for a in a8:
#     print(a)

#Zad 9 Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając z opcji “spłaszczenia” macierzy. uzyj funkcji
# flat()

# a9 = np.array([[1,1,1],[2,2,2],[3,3,3]])
#
# for b in a9.flat:
#     print(b)
#     print("")
#
#zad 10 Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?
