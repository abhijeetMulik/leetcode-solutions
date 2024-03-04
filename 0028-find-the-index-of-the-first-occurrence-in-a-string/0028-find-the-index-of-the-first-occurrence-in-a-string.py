class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:  # Handle empty needle case
            return -1

        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if haystack[i:i + n] == needle:  # Check for exact match
                return i
        return -1
                
            
