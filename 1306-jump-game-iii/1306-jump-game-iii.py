class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([(start, arr[start])]) #index, val
        seen = {(start)} #index
        n = len(arr)

        while q:
            index, val = q.popleft()
            if val == 0:
                return True

            high = index + arr[index]
            low = index - arr[index]

            if (0 <= high < n) and high not in seen:
                seen.add(high)
                q.append((high, arr[high]))
            
            if (0 <= low < n)  and low not in seen:
                seen.add(low)
                q.append((low, arr[low]))
        
        return False