class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        for i, x in enumerate(nums):
            if target - x not in pair:
                pair[x] = i
            else:
                return [i, pair[target - x]]
        return False