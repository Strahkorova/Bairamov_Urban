import csv


def get_cities_with_letter(letter):
    visited_cities = set()
    wanted_cities = set()
    with open('travel_notes.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]
            if name.startswith(letter):
                visited_cities.update(row[1].split(';'))
                wanted_cities.update(row[2].split(';'))
    return visited_cities, wanted_cities


def get_not_visited_cities(visited_cities, wanted_cities):
    return wanted_cities - visited_cities


def write_holiday_cities(first_letter):
    visited_cities, wanted_cities = get_cities_with_letter(first_letter)
    not_visited_cities = get_not_visited_cities(visited_cities, wanted_cities)
    next_city = sorted(not_visited_cities)[0] if not_visited_cities else None

    with open('holiday.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Посетили:'] + sorted(visited_cities))
        writer.writerow(['Хотят посетить:'] + sorted(wanted_cities))
        writer.writerow(['Никогда не были в:'] + sorted(not_visited_cities))
        writer.writerow(['Следующим городом будет:', next_city])


if __name__ == '__main__':
    # Пример вызова функции с буквой "L"
    write_holiday_cities('L')
