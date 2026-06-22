class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for items in nums:
            count[items] = count.get(items, 0) + 1
        
        sorted_num = sorted(count.items(), key = lambda x: x[1], reverse = True)

        result = []

        for num, freq in sorted_num[:k]:
            result.append(num)
        
        return result