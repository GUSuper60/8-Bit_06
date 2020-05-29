def lcs(a,b):
    arr=[[0]*(len(a)+1) for _ in range(len(b)+1)]
    s=""
    for i in range(len(b)):
        for j in range(len(a)):
            if(a[j]==b[i]):
                arr[i+1][j+1]=arr[i][j]+1 
                
            else:
                arr[i+1][j+1]=max(arr[i+1][j],arr[i][j+1])
    x=arr[-1][-1]
    i=len(b)
    j=len(a)
    while(x>0):
        if(a[j-1]==b[i-1]):
            s+=a[j-1]
            x-=1
            i-=1
            j-=1 
        elif(arr[i-1][j]>arr[i][j-1]):
            i-=1
        else:
            j-=1
    s=str(s[::-1])
    return (s,arr[-1][-1])
a=input()
b=input()
print(lcs(a,b))