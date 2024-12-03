class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        start, end, count = 0, 0, 0
        i = 0
        n = len(clips)

        while start < time:
            while i < n and clips[i][0] <= start:
                end = max(end, clips[i][1])
                i += 1
            if start == end:
                return -1 

            count += 1
            start = end
            
        return count

        