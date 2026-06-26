class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sortedStrs=''.join(sorted(s))
            res[sortedStrs].append(s)
        return list(res.values())