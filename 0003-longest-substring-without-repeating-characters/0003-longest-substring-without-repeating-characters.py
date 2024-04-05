class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        mymap ={}
        start = 0

        for i in range(len(s)):
            if s[i] in mymap and mymap[s[i]] >= start:
                start = max(start, mymap[s[i]]+1)
            mymap[s[i]] = i

            length = max(length, i -start+1)
        return length



        # O{n^2}
        # length = 0
        # res = []
        # for i in range(len(s)):
        #     if s[i] not in res:
        #         res.append(s[i])
        #         length = max(length, len(res))
        #     else:
        #         indx = res.index(s[i])
        #         tmp = ''.join(res[indx+1:])
        #         res.clear()
        #         if tmp != '':
        #             res.extend(tmp)
        #         res.append(s[i])
        #         print('res:', res)
        # return length


        