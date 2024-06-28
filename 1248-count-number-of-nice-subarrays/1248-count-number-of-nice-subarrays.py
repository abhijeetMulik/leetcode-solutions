class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = curr =  0
        count = defaultdict(int)
        count[0] = 1

        for i in nums:
            curr += i % 2
            ans += count[curr - k]
            count[curr] += 1
            
        return ans
