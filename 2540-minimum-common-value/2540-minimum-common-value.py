class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # n1 = set(nums1)
        n2 = set(nums2)
        # print(n1)
        # print(n2)
        for i in nums1:
            if i in n2:
                return i
        return -1
        