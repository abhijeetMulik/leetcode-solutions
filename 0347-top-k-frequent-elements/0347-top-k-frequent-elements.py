class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = []
        freq = [[] for i in range(len(nums)+1)]
        for key, val in count.items():
            freq[val].append(key)
        for i in freq[::-1]:
            for n in i:
                result.append(n)
                k -= 1
            if k == 0:
                return result
                
                
        




        # count = Counter(nums)
        # cSort = sorted(count.values(), reverse=True)
        # maxVal = cSort[0:k]
        # result =[]
        # for key, val in count.items():
        #     if k != 0 and val in maxVal:
        #         result.append(key)
        #         k -= 1
        # return result
        
