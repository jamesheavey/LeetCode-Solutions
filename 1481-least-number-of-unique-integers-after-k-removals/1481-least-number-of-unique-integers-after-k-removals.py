class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        # count the occurences of each element in the list
        count = {}
        for x in arr:
            if x not in count:
                count[x] = 1
            else:
                count[x] += 1
        
        # sum the smallest occurences until sum >= k, count how many it takes
        unique = len(count)
        values = list(count.values())
        values.sort()
        cumulative = 0
        for x in values:
            cumulative += x
            if cumulative > k:
                break
            unique -= 1
        
        return unique
                
        