class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sortedS="".join(sorted(s))
        sortedT="".join(sorted(t))

        for c in range(len(sortedS)):
            if sortedS[c] != sortedT[c]:
                return False
        
        return True
