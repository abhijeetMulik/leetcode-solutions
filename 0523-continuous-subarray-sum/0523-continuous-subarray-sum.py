class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0 : -1}
        total = 0
        for i, n in enumerate(nums):
            total += n
            rem = total % k

            if rem not in hashmap:
                hashmap[rem] = i
            elif i - hashmap[rem] >1:
                return True
            
        return False

        