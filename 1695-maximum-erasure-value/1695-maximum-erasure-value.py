class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = curr= left = 0
        dic = defaultdict(int)
        for i, n in enumerate(nums):
            if n in dic:
                while n in dic:
                    curr -= nums[left]
                    del dic[nums[left]]
                    left += 1
            dic[n] += 1
            curr += n
            ans = max(ans, curr)
        return ans
            
        