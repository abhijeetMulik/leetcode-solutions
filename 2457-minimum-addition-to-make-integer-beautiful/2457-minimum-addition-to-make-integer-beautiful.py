class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def sumtoDigits(num):
            digit = 0
            for n in str(num):
                digit += int(n)
            return digit
        
        original = n
        power_of_ten = 0

        while sumtoDigits(n) > target:
            n = n//10 + 1
            power_of_ten += 1
            
        return n * (10 ** power_of_ten) - original

        