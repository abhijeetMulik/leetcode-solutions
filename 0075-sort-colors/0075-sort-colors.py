class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def merge(arr, L, M, R):
            left = arr[L : M + 1]
            right = arr[M + 1 : R + 1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] < right[k]:
                    nums[i] = left[j]
                    j += 1
                else:
                    nums[i] = right[k]
                    k += 1
                i += 1
            
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1


        def divide(arr, l, r):
            if l == r:
                return arr
            m = (l + r) // 2
            divide(arr, l, m)
            divide(arr, m + 1, r)
            merge(arr, l, m, r)
            return arr

        divide(nums, 0, len(nums))

        