from typing import List

class subrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.ops = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.ops.append((row1, col1, row2, col2, newValue))
        
    def getValue(self, row: int, col: int) -> int:
        for op in self.ops[::-1]:
            if row >= op[0] and row <= op[2] and col >= op[1] and col <= op[3]:
                return op[4]
        return self.rectangle[row][col]