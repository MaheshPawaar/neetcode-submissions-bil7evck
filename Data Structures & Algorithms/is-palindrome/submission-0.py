class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_str = ""
        for c in s:
            if c.isalnum():
                filtered_str += c.lower()

        return filtered_str == filtered_str[::-1]