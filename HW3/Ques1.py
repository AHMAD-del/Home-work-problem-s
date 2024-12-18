"""
Question 1:
Write and test the function that attempts to remove an item from an array: 

The function searches the array a for the item key. If key is found, its first occurrence is removed; all the elements above that 
position are shifted down, size is decremented, and true is returned to indicate a successful removal. If key is not found, the array 
is left unchanged and false is returned.
"""
def removekey(key, lst):
    for i in range(1):
        if key in lst:
            lst.remove(key)
            return True
        
        return False
result = removekey(1, [1,1,2,3,1,2])                
print(result)
