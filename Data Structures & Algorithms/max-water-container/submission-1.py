class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxcapacity=0
        l=0
        r=len(heights)-1
        lentank=len(heights)
        while l<r:
            maxheight=min(heights[l],heights[r])
            currentcapacity=maxheight * (r-l)
            
            if heights[r]> heights[l]:
                l+=1
            else:
                r-=1
            maxcapacity= max(currentcapacity,maxcapacity)
        return maxcapacity
        