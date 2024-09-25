class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)

        flowerbed.append(0)
        # flowerbed.insert(0, 2)

        i = 0
        while i < length and n > 0:
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i - 1] == 0) and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            i += 1
        
        return n == 0
        