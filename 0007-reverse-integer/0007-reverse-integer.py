class Solution:
    def reverse(self, x: int) -> int:
        digits = [int(n) for n in str(x) if n != '-']
        reverse = 0
        for i in range(len(digits)):
            reverse += digits[i] * 10**i
        if x < 0:
            reverse *= -1
        
        return reverse if -2**31 <= reverse < 2**31 else 0