class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        for i in strs:
            sortedS=''.join(sorted(i))
            group[sortedS].append(i)
        return list(group.values())

        