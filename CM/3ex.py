import json
import requests
import sys


def voyage(*needed_cities, address="127.0.0.1", port=5000):
    ships = requests.get(f'http://{address}:{port}').json()
    if not ships:
        print("Ошибка выполнения запроса:")
        # print(response)
        print("Http статус:", ships.status_code, "(", ships.reason, ")")
        sys.exit(1)
    # with open('butterflies.json') as butterflies_file:
    #     ships = json.load(butterflies_file)
    # print(ships)
    # print(needed_cities)
    ships_needed = []
    for key in ships:
        current_cities = set(ships[key]) & set(needed_cities)
        if len(current_cities):
            ships_needed.append([key, len(current_cities)])
    return list(map(lambda x: x[0], sorted(ships_needed, key=lambda x: (-x[1], x[0]))))
