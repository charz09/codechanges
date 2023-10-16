from typing import List

class Solution:
    def isArraySorted(self,array, index):
        array.pop(index)
        idx = 0
        while idx < len(array)-1:
            if array[idx] > array[idx+1]:
                return False
            idx += 1
        return True
    
    def checkPossibility(self, nums: List[int]) -> bool:
    
        idx = 1
        while idx < len(nums) :
            if nums[idx] < nums[idx-1]:
                if idx == len(nums)-1:
                    return self.isArraySorted(nums, idx)
                return self.isArraySorted(nums, idx-1 if nums[idx-1] > nums[idx+1] else idx)
            idx +=1 
        
        return True 