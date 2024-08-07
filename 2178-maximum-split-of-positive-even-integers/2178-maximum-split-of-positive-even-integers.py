class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        ans = []
        if finalSum % 2:
            return ans
        num = 2
        total = 0
        while total <= finalSum:
            total += num
            ans.append(num)
            num += 2
        # print(total)
        if total > finalSum:
            ans.remove(total - finalSum)
        return ans
        