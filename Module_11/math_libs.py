import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

if __name__ == '__main__':
    # Получение текущей директории, где находится файл кода
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Путь к файлу CSV в текущей директории
    csv_file_path = os.path.join(current_directory, 'data.csv')

    # Чтение CSV файла с помощью pandas
    data = pd.read_csv(csv_file_path)

    # Преобразование данных в numpy массив
    values = data['value'].values

    # Выполнение математической операции с помощью numpy
    squared_values = np.square(values)

    # Создание графика с помощью matplotlib
    plt.plot(values, squared_values)
    plt.title('График зависимости квадрата значения от значения')
    plt.xlabel('Значение')
    plt.ylabel('Квадрат значения')

    # Путь к файлу для сохранения графика в текущей директории
    plot_file_path = os.path.join(current_directory, 'plot.png')

    # Сохранение графика в виде картинки с помощью Pillow
    plt.savefig(plot_file_path)

    # Отображение графика
    plt.show()

    # Загрузка сохраненного изображения с помощью Pillow
    img = Image.open(plot_file_path)

    # Отображение изображения
    img.show()

    # Создание массива из 5 случайных чисел от 0 до 1
    random_array = np.random.rand(5)

    # Создание массива из списка чисел
    classic_array = np.array([1, 2, 3, 4, 5])
