import argparse
# import requests
# import sys
# import json
from flask import Flask, jsonify  # , render_template, redirect, make_response, jsonify, request
import csv

parser = argparse.ArgumentParser()
parser.add_argument("arg", default=["no args"], nargs='*')
parser.add_argument("--port", default=5000, type=int)
parser.add_argument("--server", default='127.0.0.1', type=str)
parser.add_argument("--filename", default='info.csv', type=str)

args = parser.parse_args()
filename = args.filename


# print(*args.arg, sep='\n')
# print(args.shadow)
# print(args.intensity)
#
# pampasy = requests.get(f'http://{args.server}:{args.port}').json()
#
# if not pampasy:
#     print("Ошибка выполнения запроса:")
#     # print(response)
#     print("Http статус:", pampasy.status_code, "(", pampasy.reason, ")")
#     sys.exit(1)

# filename = 'info.csv'
def main1():
    with open(filename, encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter='+', quotechar='"')
        sp = []
        for index, row in enumerate(reader):
            sp.append(row[1:])
        sp = sp[1:]

    result = {}
    for row in sp:
        name = row[0] + ' ' + row[1]
        result[name] = result.get(name, []) + [row[2], row[3]]
    rs = []
    for key in result:
        dct = {'name': key, 'lie': [], 'truth': []}
        for i in range(0, len(result[key]), 2):
            if result[key][i + 1] == 'truth':
                dct['truth'].append(result[key][i])
            else:
                dct['lie'].append(result[key][i])
        rs.append(dct)
    rs = sorted(rs, key=lambda x: x['name'])
    print(rs)
    return rs


app = Flask(__name__)


@app.route('/false')
def show_city():
    rs = main1()
    print('1')
    return jsonify(rs)


# if __name__ == '__main__':
app.run(host=args.server, port=args.port)
