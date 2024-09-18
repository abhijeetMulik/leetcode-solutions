class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for s in strs:
            tmp = ''.join(sorted(s))
            if  tmp not in count:
                count[tmp] = [s]
            else:
                count[tmp].append(s)
        return count.values()

   
        