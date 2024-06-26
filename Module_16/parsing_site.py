import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Получаем HTML-код страницы CoinMarketCap
url = 'https://coinmarketcap.com/ru/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Ищем таблицу с данными о криптовалютах
table = soup.find('table', {'class': 'cmc-table'})

# Получаем строки таблицы
rows = table.find_all('tr')

# Переменные для хранения данных
cryptocurrencies = []
total_market_cap_top_100 = 0

# Обрабатываем каждую строку таблицы
for row in rows[1:101]:  # Первые 100 криптовалют (пропускаем заголовок)
    columns = row.find_all('td')
    if len(columns) > 7:
        name = columns[2].find('p').text.strip()

        # Обработка строки рыночной капитализации
        market_cap_text = columns[7].contents[0].contents[1].contents[0].replace('₽', '')
        market_cap_for_count = columns[7].contents[0].contents[1].contents[0].replace('₽', '').replace(',', '')
        try:
            market_cap_for_count = float(market_cap_for_count)
        except ValueError:
            market_cap_for_count = 0.0

        cryptocurrencies.append((name, market_cap_for_count, market_cap_text))
        total_market_cap_top_100 += market_cap_for_count

# Считаем процент от общей капитализации топ-100 криптовалют
cryptocurrencies_with_percentage = []
for name, market_cap_for_count, market_cap in cryptocurrencies:
    percentage = round((market_cap_for_count / total_market_cap_top_100) * 100, 2)
    cryptocurrencies_with_percentage.append((name, market_cap, percentage))

# Формируем название файла
now = datetime.now()
filename = now.strftime('%H.%M %d.%m.%Y') + '.csv'

# Записываем данные в CSV файл
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Название', 'Рыночная_капитализация', 'Процент_от_общей_капитализации'])
    for row in cryptocurrencies_with_percentage:
        csvwriter.writerow(row)

print(f'Данные записаны в файл {filename}')