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

    # Funkcja inicjalizująca populację losowymi osobnikami.
    def inicjalizuj_populacje(self, liczba_osobnikow, wymiar):
        
        # Parametry:
        # - liczba_osobnikow: liczba osobników w populacji
        # - wymiar: wymiar każdego osobnika, czyli ilość cech w jednym osobniku

        # Zwraca:
        # - populacja: lista zawierająca losowo wygenerowane osobniki populacji
        
        populacja = []
        
        for _ in range(liczba_osobnikow):
            # Generowanie osobnika składającego się z losowych wartości
            # w zakresie określonym przez self.zakres dla każdej cechy
            osobnik = [random.uniform(self.zakres[0], self.zakres[1]) for _ in range(wymiar)]
            
            # Dodanie wygenerowanego osobnika do populacji
            populacja.append(osobnik)
        
        # Zwrócenie populacji zawierającej wygenerowane osobniki
        return populacja
    

    # Funkcja wykonująca mutację różnicową na populacji osobników.
    def mutacja_roznicowa(self, populacja, f):
     
    # Parametry:
    # - populacja: lista zawierająca osobniki, na których będzie wykonywana mutacja
    # - f: współczynnik mutacji, określający siłę mutacji (0.7 podano)
    
    # Zwraca:
    # - nowa_populacja: lista zawierająca osobniki poddane mutacji różnicowej
    
        nowa_populacja = []
        
        # Pętla iterująca przez każdego osobnika w populacji
        for i in range(len(populacja)):
            # Losowanie trzech różnych osobników z populacji
            a, b, c = random.sample(populacja, 3)
            
            # Mutacja różnicowa na osobnikach a, b i c wg podanego wzoru
            osobnik_mut = [a[j] + f * (b[j] - c[j]) for j in range(len(a))]
            
            # Dodanie osobnika poddanego mutacji do nowej populacji
            nowa_populacja.append(osobnik_mut)
        
        # Zwrócenie nowej populacji zawierającej osobniki poddane mutacji
        return nowa_populacja


    # Funkcja wykonująca operację krzyżowania między rodzicem i mutansem.
    def krzyzowanie_osobnikow(self, parent, mutant, cr):
        
        # Parametry:
        # - parent: rodzic, czyli osobnik z populacji
        # - mutant: mutowany osobnik
        # - cr: współczynnik krzyżowania, określający szansę na wybór wartości z osobnika mutanta
        
        # Zwraca:
        # - child: nowy osobnik powstały w wyniku krzyżowania
        
        child = []
        
        # Pętla iterująca przez każdą cechę w osobnikach rodzica i mutanta
        for i in range(len(parent)):
            # Sprawdzenie, czy losowa liczba (z przedziału [0,1), dla nas 50%) jest mniejsza niż współczynnik krzyżowania
            if random.random() < cr:
                # Jeśli warunek jest spełniony, wybierz wartość z osobnika mutanta
                child.append(mutant[i])
            else:
                # W przeciwnym razie, wybierz wartość z osobnika rodzica
                child.append(parent[i])
        
        # Zwróć nowego osobnika powstałego w wyniku krzyżowania
        return child


    # Sukcesja zachłanna: Metoda wyboru nowej populacji na podstawie wartości funkcji celu
    def sukcesja_zachlanna(self, populacja, nowa_populacja):
        
        # Rozszerzenie nowej populacji o osobniki z poprzedniej populacji
        nowa_populacja.extend(populacja)
        
        # Posortowanie populacji według wartości funkcji celu dla każdego osobnika
        nowa_populacja.sort(key=lambda x: self.funkcja_celu(x))
        
        # Wybór najlepszych osobników do utworzenia nowej populacji na podstawie wartości funkcji celu
        return nowa_populacja[:len(populacja)]


 

    


