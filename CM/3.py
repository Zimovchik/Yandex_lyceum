import requests
import sys
import json


# a = {
#     "height": "average",
#     "eyes": "brown",
#     "build": "slim",
#     "hair": "short",
#     "mustache": "no",
#     "ears": "protruding",
#     "chin": "sloping"
# }


def exterior(address, port, **kwargs):
    match, mismatch = [], []
    data = requests.get(f'http://{address}:{port}').json()
    # data = a
    # match, mismatch = [], []
    # with open('trip.json') as cat_file:
    #     data = json.load(cat_file)
    for i in set(list(kwargs.keys())[:]) & set(dict(data).keys()):
        if data[i] == kwargs[i]:
            match.append(i)
        else:
            mismatch.append(i)
    match.sort()
    mismatch.sort()
    return {"match": match, "mismatch": mismatch}

# kwargs = {
#     "address": "127.0.0.1",
#     "port": 5000,
#     "eyes": "brown",
#     "build": "slim",
#     "hair": "long",
#     "mustache": "small",
#     "ears": "protruding"
# }
# # match, mismatch = [], []
# # with open('trip.json') as cat_file:
# #     data = json.load(cat_file)
# # for i in set(list(kwargs.keys())[2:]) & set(dict(data).keys()):
# #     if data[i] == kwargs[i]:
# #         match.append(i)
# #     else:
# #         mismatch.append(i)
# # match.sort()
# # mismatch.sort()
# # print({"match": match, "mismatch": mismatch})
# data = {
#     "address": "127.0.0.1",
#     "port": 5000,
#     "eyes": "brown",
#     "build": "slim",
#     "hair": "long",
#     "mustache": "small",
#     "ears": "protruding"
# }
# print(exterior(**data))
# # Данные на сервере:
