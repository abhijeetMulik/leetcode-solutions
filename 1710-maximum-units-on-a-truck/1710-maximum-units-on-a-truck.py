class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # heap = [(-n[1], n[0]) for n boxTypes]
        heap = []
        for n in boxTypes:
            heap.append((-n[1], n[0]))
        heapq.heapify(heap)
        units = 0

        while truckSize > 0 and len(heap) > 0:
            max_ele = heapq.heappop(heap)
            # condition = max_ele[1] // -max_ele[0]
            if max_ele[1] <= truckSize:
                units += -max_ele[0] * max_ele[1]
                truckSize -= max_ele[1]
            else:
                # print(truckSize)
                units += -max_ele[0] * truckSize
                break
            # print(units)
        return units
        

