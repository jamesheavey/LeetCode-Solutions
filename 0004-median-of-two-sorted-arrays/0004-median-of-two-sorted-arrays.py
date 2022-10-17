class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        join = nums1 + nums2
        join.sort()
        if len(join) % 2 == 0:
            return (join[(len(join)-1)//2] + join[len(join)//2])/2
        else:
            return join[len(join)//2]