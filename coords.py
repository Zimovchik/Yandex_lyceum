import requests


def get_coords(place):
    a = place
    geocoder_request = \
        "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=" + a + "&format=json"
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
        name = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        up = name["boundedBy"]["Envelope"]["upperCorner"]
        low = name["boundedBy"]["Envelope"]["lowerCorner"]
        up = [float(i) for i in up.split()]
        low = [float(i) for i in low.split()]
        low = abs(low[0] - up[0]), abs(low[1] - up[1])
        return low
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
