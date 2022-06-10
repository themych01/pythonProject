import pandas as pd

import numpy as np

# series
#
# s = pd.Series([1,3,5, np.nan,6,8])
# print(s)
#
# s = pd.Series([10,12,8,14], index=['Ala', 'Marek','Wiesiek','Eleonora'])
# print(s)
#
# # data frame
#
# data = {'Kraj': ['Belgia','Indie','Brazylia'],'Stolica':['Bruksela','New Delhi','Brasilia'],'Populacja':[11190846, 1303171035, 207847528]}
#
# df = pd.DataFrame(data)
# print(df)


import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(1000))
#
# # funkcja biblioteki pandas generująca skumulowaną sumę kolejnych elementów
#
# ts = ts.cumsum()
#
# print(ts)
#
# ts.plot()
# plt.show()

# wykres kolumnowy z Pandas DataFrame

# data = {'Kraj': ['Belgia','Indie','Brazylia','Polska'],'Stolica':['Bruksela','New Delhi','Brasilia','Warszawa'],
#         'Kontynent':['Europa','Azja','Ameryka Południowa','Europa'],'Populacja':[11190846, 1303171035, 207847528, 38675467]}
#
# df = pd.DataFrame(data)
#
# print(df)
#
# grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})
# print(grupa)
#
# # grupa.plot(kind='bar', xlabel='Kontynent',ylabel='MLD', rot=0, legend=True, title='Populacja z podziałem na kontynenty')
# #
# # plt.show()
#
# wykres = grupa.plot.bar()
# wykres.set_ylabel('MLD')
# wykres.set_xlabel('Kontynent')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend()
# wykres.set_title('Populacja z podziałem na kontynenty')
# # zmiana kierunku tekstu etykiet słupków
# plt.xticks(rotation=0)
# plt.savefig('wykres.png')
# plt.show()


# #Korzystając z funkcji random oraz data_range możemy wygenerować szereg czasowy danych
# ts = pd.Series(np.random.randn(1000))
# # funkcja biblioteki pandas generująca skumulowaną sumę kolejnych elementów
#
# ts = ts.cumsum()
#
# # rzutowanie Series na DataFrame
#
# df = pd.DataFrame(ts, columns=['wartości'])
# print(df)
#
# # dodanie nowej kolumny i wykorzystanie funkcji rolling do stworzenia kolejnych wartości średniej kroczącej
# df['Średnia krocząca'] = df.rolling(window=50).mean()
#
# df.plot()
# plt.legend()
# plt.show()

# # xlsx = pd.ExcelFile('imio.xlsx')
# df = pd.read_excel('imio.xlsx', header=0)
# print(df)
#
# #zad1
#
# roczniki = df['Rok'].unique()
# grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
# wykres = grupa.plot()
# wykres.set_ylabel('Liczba urodzonych dzieci')
# wykres.set_xticks(roczniki)
# wykres.tick_params(axis='x',labelrotation=40)
# wykres.legend()
# plt.subplots_adjust(left=0.15, right=0.9, bottom=0.15,top=0.9)
# plt.title("liczba urodzonych dzieci dla każdego roku")
# plt.show()


# Zad1 Za pomocą bibliotek matplotlib utwórz wykres liniowy funkcji 𝑓(𝑥)=
# 𝑥2+4 2𝑥 dla liczb całkowitych x z przedziału od
# [0,10). Dodaj odpowiednie etykiety do osi wykresu,
# tytuł linii oraz tytuł wykresu. Wyświetl legendę.
#
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
# x = np.arange(0,11,1)
#
# print(x)
#
# y = ((x**2)+4**(2*x))
#
# plt.plot(x,y, 'ro-' , label="funkcja" )
#
#
# plt.xlabel('x')
#
# plt.ylabel('Wartość')
#
# plt.title('Funkcja Kwadratowa')
#
# plt.legend()
# plt.show()

# Zad 2. (10pkt.) Za pomocą matplotlib odwzoruj siatkę
# wykresów z poniższego zdjęcia. Siatkę zapisz do pliku(imie_nazwisko_zad2.png)