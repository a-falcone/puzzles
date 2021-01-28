#!/usr/bin/env pypy3

MAX = 100000

def mex(s):
    i = 0
    while(True):
        if i not in s:
            return i
        i += 1

nim, nimr = {}, {}

for t in range(MAX + 1):
    s = set()
    i = 1
    while i**2 <= t:
        s.add(nim[t - i**2])
        i += 1
    mx = mex(s)
    nim[t] = mx
    nimr[mx] = nimr.get(mx, [])
    nimr[mx].append(t)

count = 0
for na in nimr:
    for nb in nimr:
        nc = na ^ nb
        for b in nimr[nb]:
            count += sum(a <= b for a in nimr[na]) * sum(b <= c for c in nimr.get(nc, []))
print(count)
