class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        postfix = [nums[-1]]
        ans = []

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i])
        
        for i in range(len(nums) - 2, -1, -1):
            postfix.insert(0, postfix[0] * nums[i])
        
        prefix = [1] + prefix + [1]
        postfix = [1] + postfix + [1]

        for i in range(1, len(prefix) - 1):
            ans.append(prefix[i - 1] * postfix[i + 1])

        return ans
        