class Solution:
    def myAtoi(self, s: str) -> int:
        
        # STEP 1: remove whitespace     
        s = s.strip()
        
        if len(s) < 1:
            return 0
    
        # STEP 2: read next character for + or -
        sign = -1 if s[0] == '-' else 1
        if not s[0].isdigit() and s[0] in '+-': s = s[1:]
        
        # STEP 3: read until next none digit character
        num = ''
        i = 0
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        
        # STEP 4: convert to digit, if not digits read, retrun 0
        if num == '': return 0
        
        num = sign * int(num)
        
        # STEP 5: bound the number between [-2**31, 2**31 - 1]
        
        return max(-1 * 2**31, min(2**31 -1, num))