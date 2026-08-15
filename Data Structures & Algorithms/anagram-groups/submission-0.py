class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=defaultdict(list)
        for word in strs:
            s=''.join(sorted(word))
            
            a[s].append(word)
            
                # a[s]=word
        return list(a.values())
        