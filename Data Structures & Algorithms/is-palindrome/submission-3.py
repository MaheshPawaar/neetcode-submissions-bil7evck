class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr="".join([char for char in s if char.isalnum()]).lower()
        return cleanStr == cleanStr[::-1]