class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sorted_freq = dict(sorted(freq.items(), key = lambda x: x[1], reverse = True))
        ans = []
        for k in sorted_freq:
            ans.append(k * sorted_freq[k])

        return ''.join(ans)