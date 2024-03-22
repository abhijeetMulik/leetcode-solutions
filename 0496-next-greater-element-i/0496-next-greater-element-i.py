class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in nums1:
            indx = nums2.index(i)
            n = 0
            for j in range(indx, len(nums2)):
                if nums2[j] > i:
                    result.append(nums2[j])
                    n = 1
                    break
            if n == 0: 
                result.append(-1)
        return result

        