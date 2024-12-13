# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            pick = guess(mid)
            if pick == 0:
                return mid
            if pick == 1:
                left = mid + 1
            else:
                right = mid - 1
        
        return mid
        
            


        