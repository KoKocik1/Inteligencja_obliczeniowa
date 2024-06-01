from algorytmEwolucyjny import AlgorytmEwolucyjny
from wykresy import Wykresy
import numpy as np
import math

# Parametry algorytmu
liczba_iteracji = 10000
liczba_osobnikow = 100
f = 0.7
cr = 0.5
wymiar = 3

algorymtNr=1

algorytmEwolucyjny = AlgorytmEwolucyjny()

if algorymtNr<=1:
    algorytmEwolucyjny.function=algorytmEwolucyjny.rotated_hyper_ellipsoid
    algorytmEwolucyjny.zakres=[-65.536, 65.536]
    algorytmEwolucyjny.oczekiwana_wartosc=0
    algorytmEwolucyjny.oczekiwany_zakres=[0 , 0]
    
if algorymtNr==2:
    algorytmEwolucyjny.function=algorytmEwolucyjny.power_sum_function
    algorytmEwolucyjny.zakres=[0,wymiar]
    algorytmEwolucyjny.oczekiwana_wartosc=0
    algorytmEwolucyjny.oczekiwany_zakres=[0 , 0]

if algorymtNr==3:
    algorytmEwolucyjny.function=algorytmEwolucyjny.styblinski_tang_function
    algorytmEwolucyjny.zakres=[-5,5]
    algorytmEwolucyjny.oczekiwana_wartosc=-39.16599*wymiar
    algorytmEwolucyjny.oczekiwany_zakres=[-2.903534 , 2.903534]

if algorymtNr==4:
    algorytmEwolucyjny.function=algorytmEwolucyjny.michalewicz_function
    algorytmEwolucyjny.zakres=[0,math.pi]
    algorytmEwolucyjny.oczekiwana_wartosc=[-1.80, -2.76, -3.7, -4.69, -5.69, -6.68, -7.66, -8.66, -9.66, -10.65]
    algorytmEwolucyjny.oczekiwany_zakres=[0 , 0]

if algorymtNr>=5:
    algorytmEwolucyjny.funkcja=algorytmEwolucyjny.schwefel_function
    algorytmEwolucyjny.zakres=[-500,500]
    algorytmEwolucyjny.oczekiwana_wartosc=0
    algorytmEwolucyjny.oczekiwany_zakres=[420.9687 , 420.9687]

wykresy= Wykresy()

# Inicjalizacja populacji
populacja = algorytmEwolucyjny.inicjalizuj_populacje(liczba_osobnikow, wymiar)

# Iteracje do wygenerowania wykresów
iteracje_wykres = [1, 20, 50, 100, 200, 500, 1000, 5000, 9999]

# Tworzenie osi X dla iteracji
osie_x = list(range(liczba_iteracji))

# Pętla główna ewolucji różnicowej
najlepsze_rozwiazanie_iteracji = []
srednie_rozwiazanie_iteracji = []
najgorsze_rozwiazanie_iteracji = []

# Pętla główna ewolucji różnicowej
for iteracja in range(liczba_iteracji):
    nowa_populacja = algorytmEwolucyjny.mutacja_roznicowa(populacja, f)
    for i in range(len(populacja)):
        nowa_populacja[i] = algorytmEwolucyjny.krzyzowanie_osobnikow(populacja[i], nowa_populacja[i], cr)
    populacja = algorytmEwolucyjny.sukcesja_zachlanna(populacja, nowa_populacja)
    
    if wymiar == 3:
        if iteracja in iteracje_wykres:
            wykresy.wygeneruj_wykres(f"Wykres iteracji {iteracja}", np.array(populacja))

    
    # Obliczanie wartości funkcji dla każdego osobnika
    wartosci_funkcji = [algorytmEwolucyjny.funkcja_celu(osobnik) for osobnik in populacja]
    
    # Najlepsze, średnie i najgorsze rozwiązanie w iteracji
    najlepsze_rozwiazanie = min(wartosci_funkcji)
    srednie_rozwiazanie = np.mean(wartosci_funkcji)
    najgorsze_rozwiazanie = max(wartosci_funkcji)
    
    # Dodaj wyniki do list
    najlepsze_rozwiazanie_iteracji.append(najlepsze_rozwiazanie)
    srednie_rozwiazanie_iteracji.append(srednie_rozwiazanie)
    najgorsze_rozwiazanie_iteracji.append(najgorsze_rozwiazanie)
    
# Raportowanie wyników
najlepsze_rozwiazanie = min(populacja, key=lambda x: algorytmEwolucyjny.funkcja_celu(x))
najlepsza_wartosc = algorytmEwolucyjny.funkcja_celu(najlepsze_rozwiazanie)
print("Najlepsze rozwiązanie:", najlepsze_rozwiazanie)
print("Wartość funkcji dla najlepszego rozwiązania:", najlepsza_wartosc)
print("Oczekiwana wartość:", algorytmEwolucyjny.oczekiwana_wartosc)
print(f"Oczekiwany zakres: {algorytmEwolucyjny.oczekiwany_zakres}")

wykresy.wygeneruj_wykres_rozwiazan(najlepsze_rozwiazanie_iteracji, srednie_rozwiazanie_iteracji, najgorsze_rozwiazanie_iteracji, osie_x)




