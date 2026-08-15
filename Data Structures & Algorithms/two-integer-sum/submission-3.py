class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        table={}
        for i in range(0,len(nums)):
            num=nums[i]
            diff=target-num
            if diff in table:
                return [table[diff],i]
            table[num]=i
        