class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0) + 1
        
        bucket=[[]for _ in range(n+1)]
        for key,val in freq.items():
            bucket[val].append(key)
        res=[]
        for i in range(n,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res
        return bucket