class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        totalSum = 0
        curr = 2
        ans = []
        if finalSum % 2:
            return ans
        while totalSum <= finalSum:
            totalSum += curr
            ans.append(curr)
            curr += 2
        
        if totalSum > finalSum:
            ans.remove(totalSum - finalSum)
        
        return ans
        