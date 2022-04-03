import sys

str1 = input()
data = list(map(str.strip, sys.stdin))
# data = '''VGMJUOGNTGJUKASYNN
# JUJUHIC
# JUFNHJUJU
# ADVPJBQEJRZUF'''
# data = data.split('\n')
spfind = []
cnt = 10000000
for row in data:
    fnd = row.count(str1)
    if 0 < fnd < cnt:
        spfind = []
        spfind.append(row)
        cnt = fnd
    elif fnd == cnt:
        spfind.append(row)
row = spfind[-1]
lng, fnd = 0, 0
pastfind = fnd = row.find(str1, fnd)
sp = [fnd + 1]
for i in range(cnt):
    pastfind = fnd
    fnd = row.find(str1, fnd + 1)
    if fnd == -1:
        break
    sp.append(fnd - pastfind)
sp.append(len(row) - pastfind - 1)
print(max(sp))
