class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique = set()
        seen = set()

        for i in nums:
            if i not in unique and i not in seen:
                unique.add(i)
            else:
                unique.discard(i)
                seen.add(i)
        return sum(unique)