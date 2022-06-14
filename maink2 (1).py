import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# # zad1
#
# x = np.arange(4, 20)
#
# plt.plot(x, (np.sqrt(x) + np.cos(x)) / np.sin(x))
#
# plt.title('Wykres Liniowy Funkcji')
#
# plt.xlabel('x')
# plt.ylabel('Funkcja')
#
# plt.axis([4,19,-10,40])
#
# plt.show()

# zad 2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(3.,9.,0.1)

plt.plot(x,np.tan(x)/np.sin(x),'r--',label='tan(x)/sin(x)')
plt.plot(x,np.cos(x)/np.tan(x),'g',linestyle='dotted', label='cos(x)/tan(x)')

plt.title('Wykres liniowy dwóch funkcji')

plt.ylabel('wyniki funkcji')

plt.xlabel('x')

plt.legend()

plt.show()

plt.savefig('pawel_gnyszka_zad2.png')

# zad 3
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # csv = pd.ExcelFile('flags.csv')
#
# df = pd.read_csv('flags.csv', header=0, sep=";")
#
# kontynenty = df[(df.Landmass == 'Europe') | (df.Landmass == 'South America')]
#
# religie = df.groupby(['Religion']).agg({'Population':['sum']})
#
#
# print(kontynenty)
#
# print(religie)
#
# wykres = religie.plot.bar()
# wykres.set_ylabel('Mld')
# wykres.set_xlabel('Religja')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend()
# wykres.set_title('Populacja względem Religii')
#
# plt.axis([-1, 8,0,1500])
#
# plt.show()


# # # zad 4
# #
# import pandas as pd
# import matplotlib.pyplot as plt
#
#
#
# df = pd.read_csv('flags.csv', header=0, sep=";")
#
# religie = df.groupby('Religion')['Population'].sum()
#
# print(religie)
#
#
# # wedges, texts, autotext = plt.pie(x=religie, labels=religie.index,
# #                                   autopct=lambda pct: "{:.2f}%".format(pct), textprops=dict(color='black'), shadow=True)
#
# religie.plot(kind='pie', subplots=True, autopct='%.2f' ,fontsize=14)
#
#
# plt.title("Procentowy Religi na świecie")
#
# plt.ylabel('')
#
# plt.legend()
# plt.show()
#
#
