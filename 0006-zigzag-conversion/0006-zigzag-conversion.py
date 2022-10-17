class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        zz = [[] for i in range(numRows)]
        row = col = 0
        
        while s != '':
            
            if col % (numRows-1) == 0:
                zz[row].append(s[0])
                s = s[1:]
            elif row == numRows-1-(col%(numRows-1)):
                zz[row].append(s[0])
                s = s[1:]
                
            row += 1
            row = row % numRows
            if row == 0:
                col += 1
                
        zz_string = ''
        for x in zz:
            zz_string += ''.join(x)
            
        return zz_string
            