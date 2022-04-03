import csv
import json

namefile = input()
# namefile = 'trips.csv'

with open(namefile, encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter='.', quotechar='"')
    sp = []
    for index, row in enumerate(reader):
        sp.append(row[1:-1])
sp = sorted(sp[1:], key=lambda x: (x[1], x[0]))
for index, row in enumerate(sp):
    sp[index] = {'city': row[1], 'ship': row[0]}
with open('late.json', 'w') as file:
    json.dump(sp, file)