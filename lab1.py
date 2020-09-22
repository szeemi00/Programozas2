import numpy as np
import math
import random
#EX1
def min_max(l):
    max=-math.inf
    min=math.inf
    for i in l:
        if i>max:
            max=i
    for j in l:
        if j<min:
            min=j
    print(l)
    if max!=-math.inf and min!=math.inf:
        return (f"sor maximuma:{max}, sor minimuma:{min}")
    else:
        return "error"
l=np.random.randint(0,30,20)
print(min_max(l))

#EX2
def alakzat(sorok):
    max=(sorok//2)+1
    csillag=" * "
    s=""
    for i in range (sorok+1):
        if i>=0 and i<=max:
            s+=i*csillag+"\n"
    for j in range (sorok,0,-1):
        if j>0 and j<max:
            s+=j*csillag+"\n"
    return s
print(alakzat(9))

#EX3
def matrix(m, n):
    mtx=np.ndarray((m,n))
    for i in range(m):
        for j in range(n):
            mtx[i][j]=i*j
    return mtx
print(matrix(3,4))
#row=m i, colum=n j
