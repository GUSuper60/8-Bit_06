""" https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/ """

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count=result=0
        for i in range(len(nums)):
            if(i==0 or nums[i]>nums[i-1]):
                count+=1
            else:
                result=max(result,count)
                count=1
        return max(result,count)