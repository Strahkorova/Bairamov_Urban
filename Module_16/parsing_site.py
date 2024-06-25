# -*- coding: utf8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from datetime import datetime
import time

# Путь к chromedriver
driver_path = "C:/Users/Jo/Desktop/Urban/Listen_1/Bairamov_Urban/Module_16/chromedriver.exe"  # Укажите путь к вашему chromedriver

# Инициализируем веб-драйвер
driver = webdriver.Chrome(executable_path=driver_path)
#driver = webdriver.Chrome()

# Открываем страницу CoinMarketCap
url = 'https://coinmarketcap.com/ru/'
driver.get(url)

# Даем странице загрузиться
time.sleep(10)  # Ожидание, чтобы страница полностью загрузилась

# Находим таблицу с данными о криптовалютах
table = driver.find_element(By.CLASS_NAME, 'cmc-table')

# Получаем строки таблицы
rows = table.find_elements(By.TAG_NAME, 'tr')

# Переменные для хранения данных
cryptocurrencies = []
total_market_cap_top_100 = 0

# Обрабатываем каждую строку таблицы
for row in rows[1:101]:  # Первые 100 криптовалют (пропускаем заголовок)
    columns = row.find_elements(By.TAG_NAME, 'td')
    if len(columns) > 6:
        name = columns[2].find_element(By.TAG_NAME, 'p').text.strip()
        market_cap = columns[7].text.strip().replace('₽', '').replace(',', '')

        # Преобразуем капитализацию в число
        try:
            market_cap = float(market_cap)
        except ValueError:
            market_cap = 0.0

        cryptocurrencies.append((name, market_cap))
        total_market_cap_top_100 += market_cap

# Проверка, чтобы избежать деления на ноль
if total_market_cap_top_100 == 0:
    print("Ошибка: Общая рыночная капитализация топ-100 криптовалют равна нулю.")
else:
    # Считаем процент от общей капитализации топ-100 криптовалют
    cryptocurrencies_with_percentage = []
    for name, market_cap in cryptocurrencies:
        percentage = (market_cap / total_market_cap_top_100) * 100
        cryptocurrencies_with_percentage.append((name, market_cap, percentage))

    # Формируем название файла
    now = datetime.now()
    filename = now.strftime('%H.%M %d.%m.%Y') + '.csv'

    # Записываем данные в CSV файл
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=' ')
        csvwriter.writerow(['Название', 'Рыночная_капитализация', 'Процент_от_общей_капитализации'])
        for row in cryptocurrencies_with_percentage:
            csvwriter.writerow(row)

    print(f'Данные записаны в файл {filename}')

# Закрываем веб-драйвер
driver.quit()