class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]
        for i in nums:
            prefix.append(prefix[-1] + i)
        prefix.append(0)

        left = prefix[0]
        total = prefix[-2]

        for i in range(len(nums)):
            total -= nums[i]
            if total == left:
                return i
            left += nums[i]
        return -1
        