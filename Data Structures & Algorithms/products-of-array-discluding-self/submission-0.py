class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        result = [1] * n
        prefix = 1
        postfix = 1

        for items in range(n):
            result[items] = prefix
            prefix = prefix * nums[items]
        
        for items in range(n-1, -1, -1):
            result[items] = result[items] * postfix
            postfix = postfix * nums[items]
        
        return result