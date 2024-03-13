import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Wykresy:
    def wygeneruj_wykres_rozwiazan(self, najlepsze_rozwiazanie_iteracji, srednie_rozwiazanie_iteracji, najgorsze_rozwiazanie_iteracji, osie_x):
        
        for podzial in [10,100,1000,10000]:
            # Tworzenie wykresu
            plt.plot(osie_x[:podzial], najlepsze_rozwiazanie_iteracji[:podzial], label=f'Najlepsze pierwsze {podzial}')
            plt.plot(osie_x[:podzial], srednie_rozwiazanie_iteracji[:podzial], label=f'Średnie pierwsze {podzial}')
            plt.plot(osie_x[:podzial], najgorsze_rozwiazanie_iteracji[:podzial], label=f'Najgorszepierwsze {podzial}')
            plt.grid(True)
            
            # Dodawanie tytułu i etykiet osi
            plt.title('Wyniki Ewolucji Różnicowej')
            plt.xlabel('Iteracja')
            plt.ylabel('Wartość funkcji')
            plt.legend()
            plt.show()


    def wygeneruj_wykres(self, nazwa, punkty):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_title(nazwa)
        ax.set_xlabel('Wymiar X')
        ax.set_ylabel('Wymiar Y')
        ax.set_zlabel('Wymiar Z')
        
        # Ustawienie zakresu dla każdej osi
        # ax.set_xlim(-65.536, 65.536)
        # ax.set_ylim(-65.536, 65.536)
        # ax.set_zlim(-65.536, 65.536)
        
        ax.scatter(punkty[:,0], punkty[:,1], punkty[:,2], color='blue')
        plt.show()