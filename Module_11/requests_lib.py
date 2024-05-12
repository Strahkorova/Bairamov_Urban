import requests


def pretty_print_fact(fact_data: dict) -> None:
    print("=" * 50)
    for fact_info in fact_data['data']:
        fact = fact_info['fact']
        length = fact_info['length']
        print(f"Fact: {fact}")
        print(f"Length: {length}")
        print("=" * 50)


def get_payload(page_number: int, limit: int = 5) -> dict:
    return {"limit": f"{limit}", "page": f"{page_number}"}


# Адрес (конечная точка / endpoint)
url = "https://catfact.ninja/facts"

# Заголовки запроса
headers = {
    'accept': 'application/json',  # Исправленное определение заголовков
}

if __name__ == '__main__':
    for i in range(1, 5):
        response = requests.get(url, params=get_payload(i), headers=headers)

        print(pretty_print_fact(response.json()))

        # второй вариант, чтобы не создавать лишнюю переменную если надо сразу вывести
        # print(pretty_print_fact(requests.get(url, params=get_payload(i), headers=headers).json()))
