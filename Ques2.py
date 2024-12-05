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
        if salary == -1 :
            exit
        if salary:
         # as we divide 100 / 4 = 25 is 25% of 100  then we divide 100 / 11 = 9 which means that it will give 9%
            salepercent = salary * 0.09  
            comission = 200 + int(salepercent)
            print(f"Salary is Rs. {comission}")
        
    except ValueError:
        print("Not a Integer!")   
