class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ### Appreach 1 ###
        '''
        Map the string to the designated rows in the correct order and join the rows at the end
        '''
#         if numRows == 1:
#             return s
            
#         zz = [[] for i in range(numRows)]
#         row = col = 0
        
#         while s != '':
            
#             if col % (numRows-1) == 0:
#                 zz[row].append(s[0])
#                 s = s[1:]
#             elif row == numRows-1-(col%(numRows-1)):
#                 zz[row].append(s[0])
#                 s = s[1:]
                
#             row += 1
#             row = row % numRows
#             if row == 0:
#                 col += 1
                
#         zz_string = ''
#         for x in zz:
#             zz_string += ''.join(x)
            
#         return zz_string
        
        
        ### Approach 2 ###
        '''
        There is s a repeating index pattern to map the string to the zig zag string
        increase the index to numRows, then decrease the index to 1 and repeat to end of string
        join the rows of characters at the end
        '''
        
        if numRows == 1:
            return s
            
        row_arr = [""] * numRows
        row_idx = 1
        going_up = True

        for ch in s:
            row_arr[row_idx-1] += ch
            if row_idx == numRows:
                going_up = False
            elif row_idx == 1:
                going_up = True
            
            if going_up:
                row_idx += 1
            else:
                row_idx -= 1
        
        return "".join(row_arr)