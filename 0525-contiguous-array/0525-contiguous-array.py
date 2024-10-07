class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans, count = 0, 0
        hashmap = {}

        for i, n in enumerate(nums):
            if n == 0:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                ans = max(ans, i + 1)
            
            if count not in hashmap:
                hashmap[count] = i
            else:
                ans = max(ans, i - hashmap[count])

        return ans
        