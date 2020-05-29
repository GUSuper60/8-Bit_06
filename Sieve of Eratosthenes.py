def solution(n):
    a=[]
    for i in range(n):
        if(i%2==0):
            a.append(0)
        else:
            a.append(1)
    i=3
    while(i<n):
        j=i*i
        while(j<n):
            a[j]=0
            j=j+i 
        i=i+1 
    a[2]=1
    a[0]=a[1]=0
    for i in range(n):
        if(a[i]==1):
            print(i,end=" ")
n=int(input())
solution(n)