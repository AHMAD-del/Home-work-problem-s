"""
Task 5:
Write a program that reads in a find out the total number of digits, blank spaces, punctuations, upper and lower case letters from 
a character array of size 20

"""
from string import ascii_lowercase, ascii_uppercase, whitespace, digits, punctuation
lwrcse =0
upprcse = 0
space = 0
dig = 0
punc = 0
line = "PuCiT 111 – 923 – 923."
for i in line:
    if i in ascii_lowercase:
        lwrcse +=1
    if i in ascii_uppercase:
        upprcse +=1
    if i in whitespace:
        space +=1
    if i in digits:
        dig +=1
    if i in punctuation:
        punc +=1
print(f"Total number of digits: {dig}\nTotal number of blank spaces: {space}")
print(f"Total number upper case character: {upprcse}, Total number lower case: {lwrcse}")
