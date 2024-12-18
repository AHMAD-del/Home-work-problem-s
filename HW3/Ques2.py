"""Write and test the function: 
The function rotates the elements of the array a, number of positions to the right (or number of positions to the left if k is 
negative). The last positions elements are wrapped around to the beginning of the array. 
For example, 
1. The call rotate(a,8,3) would transform the array 
{22,33,44,55,66,77,88,99} into {77,88,99,22,33,44,55,66} 
2. The call rotate(a,8,4) would transform the array 
{22,33,44,55,66,77,88,99} into {66,77,88,99,22,33,44,55}"""

def rotate(lst,len, positions):
    newlst = []
    for i in range(len):
        newlst.append(lst[-positions])
        # lst.remove(-positions)
        positions -= 1
    return newlst


result = rotate([1,2,3,4,5,6,7,8,9], 9, 1)
print(result)
