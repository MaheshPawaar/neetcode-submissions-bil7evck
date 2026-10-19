class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedStr=re.sub(r'[^a-zA-Z0-9]','',s).lower()

        l=0
        r=len(cleanedStr)-1

        while l<r:
            if cleanedStr[l]!=cleanedStr[r]:
                return False
            l+=1
            r-=1
        return True