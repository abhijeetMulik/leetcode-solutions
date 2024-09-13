class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            currSum = numbers[left] + numbers[right]
            if currSum == target:
                return [left + 1, right + 1]
            if currSum > target:
                right -= 1
            else:
                left += 1

        # for i in range(len(numbers)):
        #     noToFind = target - numbers[i]
        #     if noToFind in numbers:
        #         j = numbers.index(noToFind)
        #         if numbers[i] == numbers[j]:
        #             j += 1
        #         return [i+1, j+1]



        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
                
        