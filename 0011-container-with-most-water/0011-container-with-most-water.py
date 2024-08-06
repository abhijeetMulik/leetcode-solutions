class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        water = 0
        while left < right:
            container = min(height[left], height[right]) * (right - left)
            water = max(water, container)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return water

            



        