class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        count = collections.Counter()
        for start, destination in paths:
            count[start] += 1

        for start, destination in paths:
            if destination in count:
                count[destination] -= 1
                if count[destination] == 0:
                    del count[destination]
            else:
                return destination

        