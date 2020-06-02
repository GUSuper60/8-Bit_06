# https://leetcode.com/problems/partition-equal-subset-sum/submissions/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=0
        for i in nums:
            s+=i
        if(s%2!=0):
            return(False)
        else:
            arr=[[False]*((s//2)+1) for _ in range(len(nums)+1)]
            for i in range(len(nums)+1):
                for j in range((s//2)+1):
                    if(j==0):
                        arr[i][j]=True
                    elif(j<nums[i-1]):
                        arr[i][j]=arr[i-1][j]
                    else:
                        arr[i][j]=(arr[i-1][j] or arr[i-1][j-nums[i-1]])
            return (arr[-1][-1])
