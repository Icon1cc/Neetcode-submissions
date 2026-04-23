class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
         first = 0
         for item in nums:
            if item != val:
                nums[first] = item
                first += 1
        
         return first
