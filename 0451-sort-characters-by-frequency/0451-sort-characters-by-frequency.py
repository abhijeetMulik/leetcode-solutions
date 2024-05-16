class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        ans = []
        sorted_dic = dict(sorted(freq.items(), key=lambda item: item[1], reverse = True))
        for k, v in sorted_dic.items():
            c = 0
            while c != v:
                ans.append(k)
                c += 1

        return ''.join(ans)
        