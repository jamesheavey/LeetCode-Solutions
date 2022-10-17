class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # join = nums1 + nums2
        # join.sort()
        # if len(join) % 2 == 0:
        #     return (join[(len(join)-1)//2] + join[len(join)//2])/2
        # else:
        #     return join[len(join)//2]
        

        m, n = len(nums1), len(nums2)
        mid = (m + n) // 2 + 1
        prev2 = prev1 = None
        i = j = 0

        for _ in range(mid):
            prev2 = prev1
            if j == n or (i != m and nums1[i] <= nums2[j]):
                prev1 = nums1[i]
                i += 1
            else:
                prev1 = nums2[j]
                j += 1
        
        return prev1 if (m + n) % 2 else (prev1 + prev2) / 2