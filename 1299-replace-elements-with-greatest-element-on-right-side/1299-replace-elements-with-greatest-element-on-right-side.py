class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp = -1
        for i in range(len(arr)-1, -1, -1):
            newMax = max(arr[i], temp)
            arr[i] = temp
            temp = newMax
        return arr
        
        