class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res={}
        for i in range(len(names)):
            res[heights[i]]=names[i]
        result=sorted(res, reverse=True)
        return [res[heights] for heights in result]

        