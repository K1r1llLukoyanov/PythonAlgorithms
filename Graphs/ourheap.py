from typing import Any

class OurHeap(object):
    def __init__(self, data: list[tuple[float, int]]) -> None:
        self.data = data
        
    def update(self, old_value: tuple[float, int], new_value: tuple[float, int]) -> None:
        i = 0
        for i in range(len(self.data)):
            if self.data[i][1] == old_value[1]:
                break
        if i == len(self.data):
            self.data.append(new_value)
        else:
            del self.data[i]
            self.data.append(new_value)

    def pop(self) -> tuple[float, int]:
        min_dist = float('inf')
        ind = 0
        for i in range(len(self.data)):
            if self.data[i][0] <= min_dist:
                min_dist = self.data[i][0]
                ind = i
        data = self.data[ind]
        del self.data[ind]
        return data