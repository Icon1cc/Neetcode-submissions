class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mylist = set()
        for items in nums:
            if items in mylist:
                return True
            mylist.add(items)
        return False