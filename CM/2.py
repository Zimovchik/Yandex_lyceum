import csv
import json

fl = input()
with open(fl, encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    a = []
    for index, row in enumerate(reader):
        a.append(row[1:])
a = sorted(a[1:], key=lambda x: (int(x[-1]), x[0]))
for i, row in enumerate(a):
    a[i] = {"city": row[0], "transport": row[1], "time": row[2]}
print(a)
with open("trip.json", "w") as f:
    json.dump(a, f)
