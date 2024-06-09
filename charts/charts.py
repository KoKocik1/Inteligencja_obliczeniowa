import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from PIL import Image


class Charts:

    def __init__(self) -> None:
        self.z_grid = None
        self.x_range = None
        self.y_range = None
        self.charts = []
        self.finalCharts = []

    def generate_final_chart(self, best_solution_of_iteration, midium_solution_of_iteration, worst_solution_of_iteration, x_axis):

        for split in [10, 100, 1000, 10000]:
            plt.cla()
            plt.figure()

            plt.plot(x_axis[:split], best_solution_of_iteration[:split],
                     label=f'Best: {split}')
            plt.plot(x_axis[:split], midium_solution_of_iteration[:split],
                     label=f'Midium: {split}')
            plt.plot(x_axis[:split], worst_solution_of_iteration[:split],
                     label=f'Worst: {split}')
            plt.grid(True)
            plt.title('Differention evolution results')
            plt.xlabel('Iteration')
            plt.ylabel('Value')
            plt.legend()
            plt.show()

    # def generate_chart(self, name, points, func, x_range=None, y_range=None):
    #     fig = plt.figure(figsize=(8, 6))
    #     ax = fig.add_subplot(111, projection='3d')
    #     ax.set_title(name)
    #     ax.set_xlabel('X')
    #     ax.set_ylabel('Y')
    #     ax.set_zlabel('Z')

    #     # Ustalanie zakresu dla funkcji
    #     if x_range is not None:
    #         x_min, x_max = x_range
    #     else:
    #         x_min, x_max = np.min(points[:, 0]), np.max(points[:, 0])

    #     if y_range is not None:
    #         y_min, y_max = y_range
    #     else:
    #         y_min, y_max = np.min(points[:, 1]), np.max(points[:, 1])

    #     # Generowanie wartości funkcji
    #     x_vals = np.linspace(x_min, x_max, 100)
    #     y_vals = np.linspace(y_min, y_max, 100)
    #     x_grid, y_grid = np.meshgrid(x_vals, y_vals)
    #     z_vals = np.array([func([x, y])
    #                       for x, y in zip(np.ravel(x_grid), np.ravel(y_grid))])
    #     z_grid = z_vals.reshape(x_grid.shape)

    #     # Rysowanie powierzchni funkcji
    #     ax.plot_surface(x_grid, y_grid, z_grid, color='r', alpha=0.5)

    #     # Rysowanie punktów - obliczanie wartości z dla punktów
    #     z_points = np.array([func([x, y]) for x, y in points[:, :2]])
    #     ax.scatter(points[:, 0], points[:, 1], z_points, color='blue', s=10)

    #     # Ustawianie zakresu osi Z na podstawie zakresu funkcji
    #     z_min, z_max = np.min(z_vals), np.max(z_vals)
    #     ax.set_zlim(z_min, z_max)

    #     # Wyświetlanie na pełnym ekranie
    #     # mng = plt.get_current_fig_manager()
    #     # mng.full_screen_toggle()
    #     plt.show()

    def generate_chart(self, name, points, func, x_range=None, y_range=None):
        fig = plt.figure(figsize=(16, 9))
        ax = fig.add_subplot(111, projection='3d')
        ax.set_title(name)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Ustalanie zakresu dla funkcji
        if x_range is not None:
            x_min, x_max = x_range
        else:
            x_min, x_max = np.min(points[:, 0]), np.max(points[:, 0])

        if y_range is not None:
            y_min, y_max = y_range
        else:
            y_min, y_max = np.min(points[:, 1]), np.max(points[:, 1])

        # Generowanie wartości funkcji
        x_vals = np.linspace(x_min, x_max, 100)
        y_vals = np.linspace(y_min, y_max, 100)
        x_grid, y_grid = np.meshgrid(x_vals, y_vals)
        z_vals = np.array([func([x, y])
                          for x, y in zip(np.ravel(x_grid), np.ravel(y_grid))])
        z_grid = z_vals.reshape(x_grid.shape)

        # Rysowanie powierzchni funkcji
        ax.plot_surface(x_grid, y_grid, z_grid, color='r', alpha=0.5)

        # Rysowanie punktów - obliczanie wartości z dla punktów
        z_points = np.array([func([x, y]) for x, y in points[:, :2]])
        ax.scatter(points[:, 0], points[:, 1], z_points, color='blue', s=10)

        # Ustawianie zakresu osi Z na podstawie zakresu funkcji
        z_min, z_max = np.min(z_vals), np.max(z_vals)
        ax.set_zlim(z_min, z_max)

        chart_file = f'img/{name}.png'
        self.charts.append(chart_file)
        fig.savefig(chart_file)

    # def display_charts(self):
    #     num_charts = len(self.charts)
    #     if num_charts == 0:
    #         print("Brak wykresów do wyświetlenia.")
    #         return

    #     for i in num_charts:
    #         chart_data = Image.open(self.charts[i])
    def display_charts(self):
        num_charts = len(self.charts)
        if num_charts == 0:
            print("Brak wykresów do wyświetlenia.")
            return

        # Wczytanie wszystkich zapisanych wykresów
        images = [Image.open(chart) for chart in self.charts]

        # Obliczanie łącznej wysokości nowego obrazu
        total_height = sum(image.height for image in images)
        max_width = max(image.width for image in images)

        # Tworzenie nowego obrazu o odpowiednim rozmiarze
        combined_image = Image.new('RGB', (max_width, total_height))

        # Wklejanie kolejnych wykresów jeden pod drugim
        y_offset = 0
        for image in images:
            combined_image.paste(image, (0, y_offset))
            y_offset += image.height

        # Wyświetlenie połączonego obrazu
        combined_image.show()
        # Zapisanie połączonego obrazu
        combined_image.save('img/AllCharts.png')
