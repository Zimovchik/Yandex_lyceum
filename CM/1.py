import sys
import re

search = input()
lines = list(map(str.strip, sys.stdin))
fit = list(filter(lambda x: x.count(search) == 4, lines))
if len(fit) == 0:
    print('')
    quit()
fit = fit[-1]
indexes = [m.start() for m in re.finditer(search, fit)]
print(indexes)
max_id = 0
id = 0
for i in range(len(indexes) - 1):
    if indexes[i + 1] - indexes[i] > max_id:
        max_id = indexes[i + 1] - indexes[i]
        id = i
print(fit[indexes[id]:indexes[id + 1]])
# a = max([search + g for g in fit.split(search) if g != ''], key=lambda x: (len(x), x))
# print(a)
