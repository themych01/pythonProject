import numpy as np

a = np.array([1,2,3])
print(a)

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

# gET dIMENSION
a.ndim

# get shape
b.shape

# get Type
a.dtype

# get size
a.itemsize

# Get Total size
a.nbytes

a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

# get a specific element [wiersz,kolumna] -1, -2 = oznacza pierwszy od konca , drugi od konca
a[1,5]

# get a specific row
a[0,:]

# get a specific kolumn
a[:,2]

# getting a little more fancy [startindex:endindex:stepsize]
a[0,1:6:2]


