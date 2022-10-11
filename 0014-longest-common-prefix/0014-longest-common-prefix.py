class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        common = min(strs,key=len)
        for i, ch in enumerate(common):
            for string in strs:
                if string[i] != ch:
                    return common[:i]
                    
        return common
            