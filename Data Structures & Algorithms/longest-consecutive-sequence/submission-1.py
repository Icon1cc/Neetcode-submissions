class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_list = set(nums)
        max_length = 0

        for num in new_list:
            if num-1 not in new_list:
                curr_num = num
                curr_length = 1

                while curr_num + 1 in new_list:
                    curr_num += 1
                    curr_length += 1
                max_length = max(curr_length, max_length)
        
        return max_length