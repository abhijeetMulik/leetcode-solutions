class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1]
        left = len(arr) - 1
        while len(ans) < len(arr):
            ans.append(max(ans[-1], arr[left]))
            left -= 1
        
        return ans[::-1]
    
        