class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            noToFind = target - numbers[i]
            if noToFind in numbers:
                j = numbers.index(noToFind)
                if numbers[i] == numbers[j]:
                    j += 1
                return [i+1, j+1]



        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
                
        