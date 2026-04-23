class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for items in nums:
            if count == 0:
                candidate = items
            
            if items == candidate:
                count += 1
            else:
                count -= 1
        return candidate