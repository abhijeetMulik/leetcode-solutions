class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = set()
        count = defaultdict(int)
        for i in range(len(s) - 10):
            count[s[i:i+10]] += 1
        
        for k,v in count.items():
            if v > 1:
                result.add(k)

        return list(result)

        