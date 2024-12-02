class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digitsToSum(n):
            digits = 0
            for i in str(n):
                digits += int(i)
            print(digits)
            return digits
        original = n
        power = 0
        while digitsToSum(n) > target:
            n = n//10 + 1
            power += 1
        return n * (10 ** power) - original