class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        # right = len(s)-1
        # i=0
        # while i < right:
        #     s[i], s[right] = s[right], s[i]
        #     right -=1
        #     i +=1
            
