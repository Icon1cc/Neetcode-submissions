class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for items in nums:
            if items not in seen:
                seen.add(items)
            else:
                return True
        return False