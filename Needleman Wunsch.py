# -*- coding: utf-8 -*-
import numpy as np
 
def tripleMax(a, b, c):
    temp = max(a, b)
    return max(temp, c)

def findSequenceAlignment(s1, s2, matchValue, mismatchValue, gapValue):
    table = np.zeros(shape=((len(s2)+1), (len(s1)+1)), dtype=int)
      
    for y in range(1,table.shape[0]): #fill first horizontal and first vertical entries
        table[y,0] = table[y-1,0]+gapValue
    for x in range(1,table.shape[1]):
        table[0,x] = table[0, x-1]+gapValue
        
    for y in range(1, table.shape[0]): #fill the remaining rows and columns to the right
        for x in range(1, table.shape[1]):
            s1Value = s1[x-1] #get the sequence letters for comparison below, shifted because of the different table numbering
            s2Value = s2[y-1]
            
            topValue = table[y-1,x] + gapValue #adding the penalties (careful with the positive sign, the value is already negative)
            leftValue = table[y ,x-1]  + gapValue
            topleftvalue= table[y-1, x-1]            
            
            if s1Value == s2Value: #adding the match or mismatch values
                topleftvalue += matchValue
            else:
                topleftvalue += mismatchValue
            
            table[y,x] = tripleMax(topValue, leftValue, topleftvalue)                
    print(table)
    
    #Table is now filled, start backtracking    
    y=table.shape[0]-1
    x=table.shape[1]-1
    while x>0 or y>0:

        entry = table[y,x] 
        gapPredecessor = entry - gapValue
        # matchPredecessor = entry - matchValue
        # mismatchPredecessor = entry - mismatchValue
        
        if gapPredecessor == table[y-1, x] and y>0:
            s1 = s1[:x] + "-" + s1[x:]
            y-=1            
            print("taking top value for", entry)
        elif gapPredecessor == table[y, x-1] and x>0:
            s2 = s2[:y] + "-" + s2[y:]
            x-=1            
            print("taking left value for", entry)
        else: #elif matchPredecessor == table[y-1, x-1] or mismatchPredecessor == table[y-1, x-1]:
            y-=1
            x-=1            
            print("taking topleft value for", entry)     
            
       
    return (s1, s2)
            





s1 = "TGCTCGTA"
s2 = "TTCATA"
result = findSequenceAlignment(s1, s2, 5, -2, -6)

print(result[0]+"\n"+result[1])