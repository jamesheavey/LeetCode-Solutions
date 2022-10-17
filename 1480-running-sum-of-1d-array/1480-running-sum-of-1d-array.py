class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runSum = []
        cumulative = 0
        for val in nums:
            cumulative += val
            runSum.append(cumulative)
        return runSum