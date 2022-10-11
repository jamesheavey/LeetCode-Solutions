class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
#         while(val in nums):
#             nums.remove(val)
        
#         return len(nums)

        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i