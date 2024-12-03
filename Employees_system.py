print("\n******** Welcome to Employees system of the company *********")
names = []
salaries = []
departments = []
IDs = []

while True:
    print("\n1. Add Employee\n2. Search Employee by Name\n3. Delete Employee\n4. Show All Employees\n5. Quit")
    choice = input("\n>>> Enter your choice: ")

    if choice == '1':
        print("\n*****************************************")
        name = input("\n>>> Enter employee name: ")
        salary = input("\n>>> Enter employee salary: ")
        department = input("\n>>> Enter employee department: ")
        emp_id = input("\n>>> Enter employee ID: ")

        # Add employees info to the lists
        names.append(name)
        salaries.append(salary)
        departments.append(department)
        IDs.append(emp_id)
        print("\n***** The Employee added successfully *****")
        print("\n*****************************************")

    elif choice == '2':  #search
        print("\n*****************************************")
        search_ID = input("\n>>> Enter ID of employee to search: ")
        isfound = False
        for i in range(len(IDs)):
            if IDs[i] == search_ID:
                print("\n**** Employee is found ****")
                print("\n<<< Employee information >>>")
                print("*Name:", names[i])
                print("*Salary:", salaries[i])
                print("*Department:", departments[i])
                print("*ID:", IDs[i])
                print("\n*****************************************")
                isfound = True
                break
        if not isfound:
            print("\n********The Employee you looked for not found*******")

    elif choice == '3':  #delete
        print("\n*****************************************")
        del_ID = input("Enter ID of employee to delete: ")
        isfound = False
        for i in range(len(IDs)):
            if IDs[i] == del_ID:
                del names[i]
                del salaries[i]
                del departments[i]
                del IDs[i]
                print("*******Employee deleted successfully*******")
                isfound = True
                break
        if not isfound:
            print("Employee not found!")

    elif choice == '4':
        if len(IDs) != 0:
            print("\n*****************************************")
            print("\nEmployees List:")
            for i in range(len(IDs)):
                print("Name:", names[i])
                print("Salary:", salaries[i])
                print("Department:", departments[i])
                print("ID:", IDs[i])
                print()
            
        else:
            print("\n****** There is no employees ********")
            

    elif choice == '5':
        print("Quite the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")

