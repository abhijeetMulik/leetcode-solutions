class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        cSort = sorted(count.values(), reverse=True)
        maxVal = cSort[0:k]
        result =[]
        for key, val in count.items():
            if k != 0 and val in maxVal:
                result.append(key)
                k -= 1
        return result
        
