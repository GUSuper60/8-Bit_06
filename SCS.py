#https://leetcode.com/problems/shortest-common-supersequence/submissions/

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        arr=[[0]*(len(str1)+1) for _ in range(len(str2)+1)]
        s=""
        for i in range(len(str2)):
            for j in range(len(str1)):
                if(str1[j]==str2[i]):
                    arr[i+1][j+1]=arr[i][j]+1 

                else:
                    arr[i+1][j+1]=max(arr[i+1][j],arr[i][j+1])
        x=arr[-1][-1]
        i=len(str2)
        j=len(str1)
        while(i>0 and j>0):
            if(str1[j-1]==str2[i-1]):
                s+=str1[j-1]
                x-=1
                i-=1
                j-=1 
            elif(arr[i-1][j]>arr[i][j-1]):
                s+=str2[i-1]
                i-=1
            else:
                s+=str1[j-1]
                j-=1
        while(i>0):
            s+=str2[i-1]
            i-=1
        while(j>0):
            s+=str1[j-1]
            j-=1
        s=str(s[::-1])
        return s