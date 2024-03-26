class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result =[]
        temp = set()
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                temp.add(nums1[i])
        result.append(temp)
        temp = set()
        for j in range(len(nums2)):
            if nums2[j] not in nums1:
                temp.add(nums2[j])
        result.append(temp)
        return result
                


        