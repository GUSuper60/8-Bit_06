""" Using Recursion : 0(2^n)"""

def recursive_lcs(a,b):
    i,j=0,0
    if(i>=len(a) or j>=len(b)):
        return 0
    elif(a[i]==b[j]):
        return 1+recursive_lcs(a[i+1:],b[j+1:])
    else:
        return max(recursive_lcs(a[i+1:],b[j:]),recursive_lcs(a[i:],b[j+1:]))
a="bd"
b="abcd"
print(recursive_lcs(a,b))


""" Using Dynamic Progrmming: 0(m*n) """

def mem_lcs(a,b):
    n,m=len(a),len(b)
    dp=[[0]*(m+1) for z in range(n+1)]
    for i in range(n):
        for j in range(m):
            if(a[i]==b[j]):
                dp[i+1][j+1]=dp[i][j]+1
            else:
                dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
    return dp[-1][-1]
a="bd"
b="abcd"
print(mem_lcs(a,b))
