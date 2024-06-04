class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s = s[::-1]
        right = 0
        left = len(s) - 1
        while right <= left:
            s[right], s[left] = s[left], s[right]
            right += 1
            left -= 1