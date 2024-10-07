class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i, n in enumerate(nums):
            while stack and stack[-1] > n and len(stack) + len(nums) - i > k:
                stack.pop()
            stack.append(n)
        

        return stack[:k]