class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        j = 0
        res= set()
        for i in range(len(nums)):
            if i -j > k:
                res.remove(nums[j])
                j += 1
            if nums[i] in res:
                return True
            res.add(nums[i])
        return False

        