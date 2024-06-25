class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = ans = 0
        hmap = {}
        for i, n in enumerate(nums):
            if n == 0:
                count += 1
            else:
                count -= 1
            if count == 0:
                ans = max(ans, i + 1)
            if count not in hmap:
                hmap[count] = i
            else:
                ans = max(ans, i - hmap[count])
        return ans


        