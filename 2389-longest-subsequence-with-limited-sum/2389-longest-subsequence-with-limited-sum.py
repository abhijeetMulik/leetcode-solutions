class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for n in range(1, len(nums)):
            nums[n] += nums[n - 1]
        
        left, right = 0, len(nums) - 1
        ans = []

        for q in queries:
            i = bisect_right(nums, q)
            ans.append(i)
        
        return ans

    

