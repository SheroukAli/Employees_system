employees = []
print("\n******** Welcome to Employees system of the company *********")
while True:
    print("\n1. Add Employee\n2. Search Employee by Name\n3. Delete Employee\n4. Show All Employees\n5. Quit")
    choice = input("\n>>>Enter your choice: ")
    
    if choice == '1':
        print("\n*****************************************")
        name = input(">>>Enter employee name: ")
        salary = input(">>>Enter the employee salary: ")
        department = input(">>>Enter employee department: ")
        emp_id = input(">>>Enter employee ID: ")

        
        # Create a dictionary 
        employee = {
            'Name': name,
            'Salary': salary,
            'Department': department,
            'ID': emp_id
        }
        
        
        employees.append(employee)
        print("\n******Employee added sucessfuly*******")
        
    elif choice == '2':
        print("\n*****************************************")
        search_ID = input("\n>>>Enter ID to search: ")
        isfound = False
        for employee in employees:
            if employee['ID'] == search_ID:
                print("*****Employee is found******")
                for key, value in employee.items():
                    print(key ,":", value)
                isfound = True
                break
        if not isfound:
            print("******Employee is not found*********")
    
    elif choice == '3':
        print("\n*****************************************")
        del_ID = input("\n>>>Enter ID of employee to delete: ")
        isfound = False
        for employee in employees:
            if employee['ID'] == del_ID:
                employees.remove(employee)
                print("\n*******Employee deleted successfully******")
                isfound = True
                break
        if not isfound:
            print("********Employee not found********")
   
    elif choice == '4':
        print("\n*****************************************")
        if len(employees) == 0:
            print("****** No employees in the list ********")
        else:
            print("Employee List:")
            for employee in employees:
                for key, value in employee.items():
                    print(key ,':', value)
                print()
    
    elif choice == '5':
        print("\n*****************************************")
        print("exit from the program")
        break

    else:
        print("Invalid choice, enter a valid option.")

