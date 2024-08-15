class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary_search(potions, target):
            left = 0
            right = len(potions) - 1
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return left

        potions.sort()
        ans = []
        total = len(potions)
        for spell in spells:
            index = binary_search(potions, success / spell)
            ans.append(total - index)
        return ans

        