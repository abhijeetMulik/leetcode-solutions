class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        curr = 0
        left = 0
        right = 2**(n-1)
        for i in range(1, n):
            mid = (left + right) // 2
            if k <= mid:
                right = mid
            else:
                left = mid + 1
                curr = 0 if curr else 1
        return curr


        