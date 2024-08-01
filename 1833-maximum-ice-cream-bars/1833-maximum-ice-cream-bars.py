class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        def count_sort(costs):
            max_element = max(costs)
            min_element = min(costs)
            range_of_elements = max_element - min_element + 1

            # Initialize count array
            count = [0] * range_of_elements

            # Store count of each element
            for cost in costs:
                count[cost - min_element] += 1

            # Modify count array to store the position of elements in sorted array
            for i in range(1, range_of_elements):
                count[i] += count[i - 1]

            # Build the output array
            output = [0] * len(costs)
            for cost in reversed(costs):
                output[count[cost - min_element] - 1] = cost
                count[cost - min_element] -= 1

            return output

        sorted_count = count_sort(costs)
        ans = 0
        total = 0
        for s in sorted_count:
            if total + s <= coins:
                total += s
                ans += 1
            else:
                break
      
        return ans

        