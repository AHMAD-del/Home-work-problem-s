"""
 Task 2:
One large chemicalcompany pays its salespeople on a commission basis.The salespeople receive 
Rs. 200 per week plus 9 percent of their gross sales for that week. For example, a sales
person who sells Rs. 5000 worth of chemicals in a week receives Rs. 200 plus 9 percent of 
Rs. 5000, or a total of Rs. 650. Develop a program that will input each salesperson’s gross sales for 
last week and will calculate and display that salesperson’s earnings. Process one salesperson’s figures at a time.
The program will continue its execution until a user enters a sentinel value -1. 
"""
while True:
    try:
        salary = int(input("Enter sales in rupees(-1 to end): ").strip())
        if salary:
            salepercent = salary / (11)    
            comission = 200 + int(salepercent)
            print(f"Salary is Rs. {comission}")
        else:
            print("Not int")
        if salary == -1 :
            exit
    except ValueError:
        print("Not a Integer!")   
