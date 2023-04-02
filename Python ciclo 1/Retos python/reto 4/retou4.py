import statistics as st
import numpy as np

while True:
    n, k, m = map(int,input().split())
    if n >= 1 and k >=1:
        break
med = np.empty((n,k), int)
meda= np.empty((n,k), int)
medb= np.zeros((n,k))
paco= np.zeros((n))
w = 0

for i in range(n):
    auc = list(map(int,input().split()))
    med[w] = auc
    meda[w]= auc
    w += 1

for i in range(m):
    suc, md, num, si, di = map(int,input().split())
    if (1<= suc <= n) and (0 < md <= k) and (0 < num):
        paco[suc-1] += 1
        if (si < 70) and (di < 50):
            med[suc-1][md-1]-=num
            medb[suc-1][md-1] += num
        elif (70 <= si < 110) and (50 <= di < 70):
            med[suc-1][md-1]-=0
        elif (110 <= si < 120) and (70 <= di < 75):
            med[suc-1][md-1]-=0
        elif (120 <= si < 130) and (75 <= di < 80):
            med[suc-1][md-1]-=num
            medb[suc-1][md-1] += num
        elif (130 <= si < 150) and (80 <= di < 90):
            med[suc-1][md-1]-=num
            medb[suc-1][md-1] += num
        elif (150 <= si < 170) and (90 <= di < 100):
            med[suc-1][md-1]-=num
            medb[suc-1][md-1] += num
        elif (170 <= si) and (100 <= di):
            med[suc-1][md-1]-=num
            medb[suc-1][md-1] += num
        elif (130 <= si) and (80 > di):
            med[suc-1][md-1]-=num
            medb[suc-1][md-1] += num

print('\n\n')
