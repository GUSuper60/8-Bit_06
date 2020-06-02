#https://leetcode.com/problems/subarray-sums-divisible-by-k/submissions/

from itertools import accumulate
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        arr=list(accumulate(A))
        arr=[i%K for i in arr]
        cr=[0]*K
        cr[0]=1
        for i in range(len(arr)):
            cr[arr[i]%K]+=1
        s=0
        for i in cr:
            s+=i*(i-1)//2
        return s
