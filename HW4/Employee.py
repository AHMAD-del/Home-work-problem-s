# -> Write a class named Employee for which each object can hold information about a particular employee: 
# 1. The class should have following four private data members
""" a. A string named name that holds the employee’s name. 
    b. An integer named id that holds the employee’s ID number. 
    c. A string named department that holds the name of the department where the employee works. 
    d. A string named position that holds the employee’s job title. 
"""

lst  = []

class Employee:
    def __init__(self, name='', id='', department='', position=''):
        self.name = name
        self.id = id
        self.department = department
        self.position = position

# 2. Provide the implementation of following constructors and a destructor
#     a. A constructor that accepts employee’s name, employee’s ID number, department, and position as arguments and 
#     assigns them to the appropriate member variables. 

#     b. A constructor that accepts employee’s name and ID number as arguments and assigns them to the appropriate member 
#     variables. The department and position fields should be assigned an empty string (""). 

#     c. A default constructor that assigns empty string ("") to the name, department, and position member variables, and 0
#     to the id member variable. 

#     d. A copy constructor to initialize an employee’s object with already existing object. 
#     e. A destructor that do nothing except displaying a simple message “Destructor executed…” on the screen



    

# 3. Provide the implementation of properties methods (get/set) for all the data members (name, id, department and position) of the class. 


# 4. Provide the implementation of following member functions 

    # a. setInfo method accepts employee’s name, employee’s ID number, department, and position as arguments and assigns 
    # them to the appropriate member variables. 
    # b. getInfo method to initialize the data of an employee taken from the user. 
    # c. putInfo method to display the information of a particular employee. 

    
    def setinfo(self):
        global lst
        self.name = input("Enter Name: ").strip().title()
        self.id = input("Enter ID: ").strip()
        self.department = input("Ener Department: ").strip().title()
        self.position = input("Enter Position: ").strip().title()
        lst.append({'name': self.name, 'id': self.id, 'department': self.department, 'position': self.position})

    def putinfo(self):
        global lst
        print(lst)

#   5. Once you have written the class, write main function and test its functionality a             
def main():
    
    Emp = Employee()
    Emp.setinfo()
    Emp.putinfo()


if __name__ == "__main__":
  main()
