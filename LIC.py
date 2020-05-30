#https://leetcode.com/problems/longest-increasing-subsequence/submissions/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sorted_nums=sorted(list(set(nums)))
        arr=[[0]*(len(nums)+1) for _ in range(len(sorted_nums)+1)]
        for i in range(len(sorted_nums)):
            for j in range(len(nums)):
                if(sorted_nums[i]==nums[j]):
                    arr[i+1][j+1]=arr[i][j]+1 
                else:
                    arr[i+1][j+1]=max(arr[i+1][j],arr[i][j+1])
        return arr[-1][-1]