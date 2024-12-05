"""
Task 4:
  Write a program that reads in and swap the contents of two equal size arrays named A and B of 10 elements. The program should 
  clearly show array contents and the result
"""
blst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
blst2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

alst1 = blst2.copy()
alst2 = blst1.copy()

print(f"Contents of array A before swap: {blst1}")
print(f"Contents of array B before swap: {blst2}")
print(f"Contents of array A After swap: {alst1}")
print(f"Contents of array B After swap: {alst2}")
