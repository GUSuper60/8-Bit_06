#https://leetcode.com/problems/coin-change-2/submissions/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        arr=[[0]*(amount+1) for _ in range(len(coins))]
        if(amount==0):
            return 1
        if(len(coins)==0):
            return 0
        for i in range(len(coins)):
            for j in range(amount+1):
                if(j==0):
                    arr[i][j]=1
                elif(j<coins[i]):
                    arr[i][j]=arr[i-1][j]
                else:
                    arr[i][j]=arr[i-1][j]+arr[i][j-coins[i]]
        return arr[-1][-1]
