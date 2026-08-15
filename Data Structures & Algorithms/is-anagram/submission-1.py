class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sfreq={}
        for i in s:
            sfreq[i]=sfreq.get(i,0)+1
        tfreq={}
        for j in t:
            tfreq[j]=tfreq.get(j,0)+1
        
        
        return sfreq== tfreq
        