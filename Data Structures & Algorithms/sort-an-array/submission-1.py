class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(left, right):
            if left >= right:
                return
            
            mid = (left + right) // 2

            mergeSort(left, mid)
            mergeSort(mid + 1, right)

            temp = []
            i = left
            j = mid + 1

            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= right:
                temp.append(nums[j])
                j += 1
            
            for k in range(len(temp)):
                nums[left + k] = temp[k]
        
        mergeSort(0, len(nums) - 1)

        return nums