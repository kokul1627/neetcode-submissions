class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=freq.get(i,0)+1
            else:
                return True
            
        return False
        