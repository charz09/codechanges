from typing import List

class subrectQueries:

    def __init__(self, rect: List[List[int]]):
        self.rect = rect
        self.operation = []

    def updateSubrectangle(self, rows1: int, cols1: int, rows2: int, cols2: int, newVal: int) -> None:
        self.operation.append((rows1, cols1, rows2, cols2, newVal))
        
    def getValue(self, row: int, col: int) -> int:
        for op in self.operation[::-1]:
            if row >= op[0] and row <= op[2] and col >= op[1] and col <= op[3]:
                return op[4]
        return self.rect[row][col]