#https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for i in range(len(nums)):
            c=target-nums[i]
            if(c in m):
                return [m[c],i]
            m[nums[i]]=i