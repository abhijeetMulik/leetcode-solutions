class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary_search(potions, target):
            left, right = 0, len(potions)
            while(left < right):
                mid = (left + right) // 2
                if potions[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left

        potions.sort()
        m = len(potions)
        ans = []
        for spell in spells:
            res = binary_search(potions, success / spell)
            ans.append(m - res)
        
        return ans


        