class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_str=''
        for a in s:
            if a.isalpha() or a.isdigit():
                my_str += a.lower()
        return (my_str == my_str[::-1])
        