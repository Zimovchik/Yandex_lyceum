import argparse
from flask import Flask, jsonify
import json

parser = argparse.ArgumentParser()
parser.add_argument("arg", default=["no args"], nargs='*')
parser.add_argument("--port", default=5000, type=int)
parser.add_argument("--server", default='127.0.0.1', type=str)
parser.add_argument("--filename", default='info.csv', type=str)
args = parser.parse_args()
filename = args.filename


# filename = "wear.json"


def main():
    with open(filename, encoding="utf-8") as file:
        data = json.load(file)
    keys = set([i["ethnos"] for i in data])
    ans = {i: set() for i in keys}
    for i in data:
        ans[i["ethnos"]].add(i["clothing"])
    ans = {i: sorted(list(ans[i])) for i in ans.keys()}
    return ans


app = Flask(__name__)


@app.route('/bombay')
def bruh():
    res = main()
    return jsonify(res)


app.run(host=args.server, port=args.port)
