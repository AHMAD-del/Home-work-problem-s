""" 
 Task 1:
Write a program that will take three parameters of integer type from user and display the table of the
required value from the starting limit to ending limit (starting limit < ending limit). The first 
parameter will be the table value, second will be the starting limit and third will be the ending limit.
"""
try:
    tableValue = int(input("Enter Table Value: ").strip())
    startValue = int(input("Enter Start Limit: ").strip())
    endValue = int(input("Enter End Limit: ").strip())
    if startValue > endValue:
        exit("Starting Value cann't be greater than Ending Value!")
except :
    exit("Not a integer!")
for i in range(startValue, endValue +1):
    print(tableValue * i )
