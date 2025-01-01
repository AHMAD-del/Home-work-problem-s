"""Write and test the function that attempts to add the contents of two equal size arrays: 
float * add(const float a[], const float b[], int sizeofa, int sizeofb); 
The function adds the adjacent elements of two array a and b and places there sum to the newly created array and return it if 
possible, return NULL otherwise. The addition is only possible if the sizes of both the arrays are equal. 
For example, 
1. a contains {1, 2, 3, 4, 5} and array b contains {5, 4, 3, 2, 1} then the resultant array is {6, 6, 6, 6, 6}
2. a contains {1, 2, 3, 4, 5} and array b contains {5, 4, 3, 2} then the addition is not possible so return NULL"""

def add(lst1, lst2):
    if len(lst1) == len(lst2):
        finalLst = []
        for i in range(len(lst1)):
            finalLst.append(lst1[i] + lst2[i])
        return finalLst

result = add([1, 2, 3, 4, 5],[5, 4, 3, 2, 1])
print(result)
