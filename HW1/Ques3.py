"""
Question 3:
One interesting application of computers is drawing graphs and bar charts
(sometimes called “histograms”). Write a program that reads five numbers
(each between 1 and 30). For each number read, your program should print a line
 containing that number of adjacent asterisk. 
"""
lst = []
count = 1
try:
  while count <= 5:
     lst.append(int(input(f"Enter number {count}: ")))
     count +=1
except:
 exit("Not a Number!")
for i in lst:
    print("*" * i)    
