class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        s += ' '
        
        palindrome = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                if j-i <= len(palindrome): continue
                    
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(palindrome):
                    palindrome = s[i:j]
                    
        return palindrome