#https://leetcode.com/problems/3sum/description/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            l=i+1 
            r=len(nums)-1
            while(l<r):
                if(nums[i]+nums[l]+nums[r]==0):
                    ans.append([nums[i],nums[l],nums[r]])
                    while(l<r and nums[l]==nums[l+1]):
                        l+=1
                    while(l<r and nums[r]==nums[r-1]):
                        r-=1
                    l+=1 
                    r-=1
                elif(nums[i]+nums[l]+nums[r]<0):
                    l+=1 
                else:
                    r-=1
        return ans