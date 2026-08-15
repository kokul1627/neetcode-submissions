class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s)== sorted(t):
        #     return True
        # return False
        # s=sorted(s)
        # t= sorted(t)
        hashtab={}
        for i in s:
            
            hashtab[i]=hashtab.get(i,0)+1
        for i in t:
            hashtab[i]=hashtab.get(i,0)-1
                
        for i in  hashtab:
            if hashtab[i]!= 0:
                return False
        return True