#https://leetcode.com/problems/coin-change/submissions/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr=[[sys.maxsize-1]*(amount+1) for _ in range(len(coins))]
        for i in range(len(coins)):
            for j in range(amount+1):
                if(j==0):
                    arr[i][j]=0
                elif(j<coins[i]):
                    arr[i][j]=arr[i-1][j]
                else:
                    arr[i][j]=min(arr[i-1][j],1+arr[i][j-coins[i]])
        if(arr[-1][-1]==9223372036854775806):
            return -1
        return arr[-1][-1]
        
