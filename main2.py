import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Zad1 Za pomocą bibliotek matplotlib utwórz wykres liniowy funkcji 𝑓(𝑥)=
# 𝑥2+4 2𝑥 dla liczb całkowitych x z przedziału od
# [0,10). Dodaj odpowiednie etykiety do osi wykresu,
# tytuł linii oraz tytuł wykresu. Wyświetl legendę.

# lista = []
# for x in range(0,10):
#     wynik = ((x**2+4)/(2**x))
#     lista.append(wynik)
# print(lista)


# Zad 2. (10pkt.) Za pomocą matplotlib odwzoruj siatkę
# wykresów z poniższego zdjęcia. Siatkę zapisz do pliku(imie_nazwisko_zad2.png)


# Zad 3. (6pkt) Używając biblioteki pandas wczytaj zawartość pliku „automobile.csv” do
# ramki danych i wykonaj następujące kroki:
# • Ze 100 wierszy wybranych losowo bez powtarzania utwórz nową ramkę danych
# • Na nowej ramce danych dokonaj grupowania danych po kolumnie ‘Car model’
# • Na wykresie kołowym przedstaw wielkości poszczególnych grup, wartości liczbowe na
# wykresie mają być zaokrąglone
# bez części dziesiętnych, ustaw czcionkę rozmiaru 14, dodaj etykietę do wykresu oraz
# df = pd.read_csv('automobile.csv',header=0, sep=';', decimal='.')
#
# df2 = df.sample(100)
#
# print(df2)
#
# df2.groupby('Car model')
#
# print(df2)
#
# grupy = (df2.groupby('Car model').size())
#
# print(grupy)
#
# grupy.plot(kind='pie', subplots=True, autopct='%.0f' ,fontsize=14)
#
# plt.title('Suma ilosci poszczegolnych marek')
# plt.show()




# Zad 4. (8pkt.)
# Za pomocą biblioteki pandas wczytaj zawartość pliku „automobile.csv”,
# następnie utworzysz grupę po kolumnie „Car model” i policzysz średnią
# cenę samochodów dla każdej z marek (kolumna Price), dane zobrazujesz na
# wykresie słupkowym, do stworzenia wykresu wykorzystaj bibliotekę matplotlib.
# Dodaj etykiety do osi wykresu oraz tytuł.
# Uwaga: wszystkie wykresy mają być widoczne w całości, czyli każdy element
# wykresu musi być widoczny. Wektory do zadań 1 i 2 robione za pomocą biblioteki numpy.

# df = pd.read_csv('automobile.csv',header=0, sep=';', decimal='.')
#
# grp = df.groupby(['Car model']).agg({'Price':['sum']})
#
# print(grp)