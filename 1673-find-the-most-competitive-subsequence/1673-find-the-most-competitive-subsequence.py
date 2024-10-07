class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        x = len(nums) - k
        for i, n in enumerate(nums):
            while stack and stack[-1] > n and x > 0:
                x -= 1
                stack.pop()
            stack.append(n)
        

        return stack[:k]