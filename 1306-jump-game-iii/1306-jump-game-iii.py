class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([(start)])
        seen = {start}

        def valid(index):
            return 0 <= index < len(arr)

        while queue:
            idx = queue.popleft()

            if arr[idx] == 0:
                return True
            
            inc = idx + arr[idx]
            if valid(inc) and inc not in seen:
                seen.add(inc)
                queue.append(inc)
                
            dec = idx - arr[idx]
            if valid(dec) and dec not in seen:
                seen.add(dec)
                queue.append(dec)
        
        return False

        

        