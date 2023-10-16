from typing import List

class Sol:
    def isArrayClassified(self,mainArray, idx):
        mainArray.pop(idx)
        index = 0
        while index < len(mainArray)-1:
            if mainArray[index] > mainArray[index+1]:
                return False
            index += 1
        return True
    
    def checkPossibility(self, nums: List[int]) -> bool:
    
        index = 1
        while index < len(nums) :
            if nums[index] < nums[index-1]:
                if index == len(nums)-1:
                    return self.isArraySorted(nums, index)
                return self.isArraySorted(nums, index-1 if nums[index-1] > nums[index+1] else index)
            index +=1 
        
        return True 