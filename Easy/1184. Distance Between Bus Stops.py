from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start < destination:
            path_1 = sum(distance[start:destination])
            path_2 = sum(distance[destination:]) + sum(distance[:start])
        else:
            path_1 = sum(distance[destination:start])
            path_2 = sum(distance[:destination]) + sum(distance[start:])

        return min(path_1, path_2)


distance = [14, 13, 4, 7, 10, 17, 8, 3, 2, 13]
start = 2
destination = 9
result = Solution().distanceBetweenBusStops(distance, start, destination)
print(result)
