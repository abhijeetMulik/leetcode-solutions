class Solution:
    def partitionString(self, s: str) -> int:
        seen =set()
        count = 1
        for i in s:
            if i not in seen:
                seen.add(i)
            else:
                count += 1
                seen = {i}
        return count

            
            

        