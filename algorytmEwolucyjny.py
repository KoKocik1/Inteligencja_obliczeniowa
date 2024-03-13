import random
import numpy as np
import math

class AlgorytmEwolucyjny:
    
    def __init__(self):
        self.function = self.rotated_hyper_ellipsoid
        self.zakres=[-65.536, 65.536]
        self.oczekiwana_wartosc=0
        self.oczekiwany_zakres=[0 , 0]
        
    # Definicja funkcji celu
    def funkcja_celu(self, x):
        return self.function(x)
    
    # Dostępne funkcje celu
    def rotated_hyper_ellipsoid(self,x):
        return sum([(sum(x[:i+1]))**2 for i in range(len(x))])

    def styblinski_tang_function(self,x):
        return 0.5 * sum([(i**4 - 16*i**2 + 5*i) for i in x])

    def michalewicz_function(self,x, m=10):
        return -sum([math.sin(x[i]) * math.sin((i+1) * x[i]**2 / math.pi)**(2*m) for i in range(len(x))])
    
    def power_sum_function(self,x, p=4):
        return sum([abs(x[i])**(p+i) for i in range(len(x))])
    
    def schwefel_function(self,x):
        return 418.9829 * len(x) - sum([x[i] * math.sin(math.sqrt(abs(x[i]))) for i in range(len(x))])

    # Inicjalizacja populacji losowo wg zakresu
    def inicjalizuj_populacje(self, liczba_osobnikow, wymiar):
        populacja = []
        for _ in range(liczba_osobnikow):
            osobnik = [random.uniform(self.zakres[0], self.zakres[1]) for _ in range(wymiar)]
            populacja.append(osobnik)
        return populacja

    # Mutacja różnicowa
    def mutacja_roznicowa(self, populacja, f):
        nowa_populacja = []
        for i in range(len(populacja)):
            # Losowe trzy osobniki z populacji
            a, b, c = random.sample(populacja, 3)
            # Mutacja różnicowa na osobnikach a, b i c wg podanego wzoru
            osobnik_mut = [a[j] + f * (b[j] - c[j]) for j in range(len(a))]
            # Dodanie do nowej populacji
            nowa_populacja.append(osobnik_mut)
        return nowa_populacja


    # Krzyżowanie z punktem krzyżowania CR
    def krzyzowanie_osobnikow(self, parent, mutant, cr):
        child = []
        # CR ustawione na 0,5 -> 50% szansy na wybranie wartości z osobnika mutant
        for i in range(len(parent)):
            if random.random() < cr:
                child.append(mutant[i])
            else:
                child.append(parent[i])
        return child

    # Sukcesja zachłanna: Metoda wyboru nowej populacji na podstawie wartości funkcji celu
    def sukcesja_zachlanna(self, populacja, nowa_populacja):
        # Rozszerz nową populację o osobniki z poprzedniej populacji
        nowa_populacja.extend(populacja)
        # Posortuj populację według wartości funkcji celu dla każdego osobnika
        nowa_populacja.sort(key=lambda x: self.funkcja_celu(x))
        # Wybierz najlepszych osobników do utworzenia nowej populacji na podstawie wartości funkcji celu
        return nowa_populacja[:len(populacja)]

 

    


