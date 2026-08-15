class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        zero=nums.count(0)
        if zero>1:
            return [0 for _ in range(n)]
        
        
        res=[0]*n
        for i in range(n):
            prod=1
            for j in range(n):
                if i==j:
                    continue
                prod*=nums[j]
            res[i]=prod
        return res