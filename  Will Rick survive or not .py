"""https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/will-rick-survive-or-not-2/description/"""

from itertools import accumulate
t=int(input())
while t>0:
    n=int(input())
    dis=list(map(int,input().split()))
    flag=True
    a=[0]*(max(dis)+1)
    for i in dis:
        a[i]+=1 
    a=list(accumulate(a))
    for i,v in enumerate(a):
        die=(i+1)-(i//7)
        if(v>=die):
            flag=False
            print("Goodbye Rick")
            print(die-1)
            break
    if(flag==True):
        print("Rick now go and save Carl and Judas")
    t-=1