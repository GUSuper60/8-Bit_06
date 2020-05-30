#https://www.hackerearth.com/problem/algorithm/mancunian-and-k-ordered-lcs-e6a4b8c6/submissions/

def lcs(n,m,a,b):
    arr=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if(a[i]==b[j]):
                arr[i+1][j+1]=arr[i][j]+1
            else:
                arr[i+1][j+1]=max(arr[i+1][j],arr[i][j+1])
    return arr[-1][-1]
if __name__=="__main__":
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    x=m-len(b)
    for _ in range(x):
        c=int(input())
        b.append(c)
    print(lcs(n,m,a,b)+k)