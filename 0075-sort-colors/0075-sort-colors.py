class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #   QUICKSORT

        i, l, r = 0, 0, len(nums)-1

        def swap(p, q):
            temp = nums[p]
            nums[p] = nums[q]
            nums[q] = temp

        while i <= r:
            if nums[i] == 0:
                swap(i, l)
                l +=1
            elif nums[i] ==2:
                swap(i, r)
                r -=1
                i -=1
            i +=1


        # MERGE SORT 
        # def merge(arr, L, M, R):
        #     left = arr[L:M+1]
        #     right = arr[M+1:R+1]
        #     i, j, k = L, 0, 0

        #     while j< len(left) and k < len(right):
        #         if left[j] <= right[k]:
        #             arr[i] = left[j]
        #             j +=1
        #         else:
        #             arr[i] = right[k]
        #             k +=1
        #         i += 1
        #     while j< len(left):
        #         arr[i] = left[j]
        #         j +=1
        #         i +=1
        #     while k < len(right):
        #         arr[i] = right[k]
        #         k +=1
        #         i +=1

        # def mergeSort(arr, l, r):
        #     if l==r:
        #         return arr
        #     m = (l+r)//2
        #     mergeSort(arr, l, m)
        #     mergeSort(arr, m+1, r)
        #     merge(arr, l, m, r)
        #     return arr
        # return mergeSort(nums, 0, len(nums)-1)
