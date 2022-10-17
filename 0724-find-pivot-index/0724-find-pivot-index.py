class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        max = sum(nums)
        left_sum = 0
        
        for i, val in enumerate(nums):
            if left_sum == (max - val)/2:
                return i
            left_sum += val
            
        return -1