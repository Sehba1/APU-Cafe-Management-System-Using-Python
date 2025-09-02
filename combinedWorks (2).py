def ReplaceOrDeleteLine(Filename, LineNumber, RorD, ListContent = "None"):
    if RorD == "R":
        with open(Filename, 'r') as file:
            Lines = file.readlines()
        Str = ",".join(ListContent)
        Lines = [line.strip("") for line in Lines if line.rstrip()]
        with open(Filename, 'w') as file:
            file.writelines(Lines)
    if RorD == "D":
        with open(Filename,"r") as file:
            Lines = file.readlines()
            del Lines[LineNumber - 1]
        with open(Filename, 'w') as file:
            file.writelines(Lines)

def UpdateProfile(UserList):
    if UserList[2] != "Administrator" or "Trainer" or "Lecturer":
        UserList.pop(2)
    Option = input("1.Gmail\n2.Contact Number\n3.Address\n")
    match Option:
        case "1":
            Gmail = input("New Gmail:")
            UserList[3] = Gmail
        case "2":
            ContactNumber = input("New Contact Number:")
            UserList[4] = ContactNumber
        case "3":
            Address = input("New Address:")
            UserList[5] = Address
        case _:
            print("Unknown Option")
    if UserList[2] == "Administrator" or "Trainer" or "Lecturer":
        with open("namelist - profile.txt", "r") as file:
            LineNumber = 0
            for a in file:
                a = a.split(",")
                if UserList[0] == a[0]:
                    ReplaceOrDeleteLine("namelist - profile.txt", LineNumber, "R", UserList)
                    print("Update Successfully")
                    break
                LineNumber += 1
    if UserList[2] != "Administrator" or "Trainer" or "Lecturer":
        with open("student.txt", "r") as file:
            LineNumber = 0
            for a in file:
                a = a.split("|")
                if UserList[0] == a[0]:
                    Students = read_students()
                    Students[LineNumber] = UserList
                    write_students(Students)
                    print("Update Successfully")
                    UserList.insert(2,"Student")
                    break
                LineNumber += 1
    return UserList

def Login():
    UserList = []
    Username = None
    Password = None
    detect = False
    while not detect:
        Username = input("Username:")
        with open("namelist - profile.txt", "r") as file:
            for a in file:
                a=a.strip()
                UserList = a.split(",")
                if Username == UserList[0] or Username == UserList[3]:              #a.startswith(Username):
                    Password = UserList[1]
                    detect = True
                    break
        if not detect:
            with open("student.txt", "r") as file:
                for a in file:
                    a = a.strip()
                    UserList = a.split("|")
                    if Username == UserList[0] or Username == UserList[3]:  # a.startswith(Username):
                        Password = UserList[1]
                        UserList.insert(2,"Student")
                        detect = True
                        break
        if not detect:                                                          #same as detect == False
            print("User not found")
    for a in range(3):
        password = input("Password:")
        if password == Password:
            print("Log in successfully")
            return UserList
        else:
            print("Wrong Password! Pls try again")

def DisplayProfile(UserList):
    print("{:^70}\n{:<20}:{:<20}".format("-------------------------Profile-------------------------",
                                         "Name", UserList[0], "Role", UserList[2], "Gmail", UserList[3], "Contact Number",
                                         UserList[4],"Address",UserList[5]))
    if UserList[2] == "Student":
        print("{:<20}:{:<20}\n{:<20}:{:<20}\n{:<20}:{:<20}\n{:<20}:{:<20}".format("Role", UserList[2], "Gmail",
                                                                                  UserList[4], "Contact Number",
                                                                                  UserList[5], "Address", UserList[6]))
    else:
        print("{:<20}:{:<20}\n{:<20}:{:<20}\n{:<20}:{:<20}\n{:<20}:{:<20}".format("Role", UserList[2], "Gmail",
                                                               UserList[3], "Contact Number",UserList[4],"Address",UserList[5]))
    if len(UserList)>=7:
        if UserList[2] != "Student":
            print("{:<20}:{:<20}".format("Level:",UserList[6]))
        print("Moodle:")
        Moodle = UserList[7].split("+")
        for a,moodle in enumerate(Moodle,1):
            moodle = moodle.split(".")
            print("{:<5}|{:<80}|{:<10}".format(a,moodle[0],moodle[1]))
def UserProfile(UserList):
    DisplayProfile(UserList)
    print("{:^70}".format("-------------------------Menu-------------------------"))
    match UserList[2]:                                                                  #check role
        case "Administrator":
            return "Admin"
        case "Trainer":
            return "Trainer"
        case "Lecturer":
            return "Lecturer"
        case "Student":
            return "Student"
def AssignModule():
    module = []
    print("\nModule:")
    with open("Coachingclassinformation.txt", "r") as file:
        for line in file:
            line = line.split(",")
            str = f"{line[1]}"
            if len(line) > 9:
                str += "(Additional)"
            str += "," + line[0]
            module.append(str)
    module = sorted(list(set(module)))  # all module
    List = []
    for b in module:
        b = b.split(",")
        List.append(b[0])
    List = sorted(list(set(List)))
    for a, line in enumerate(List, 1):
        print(f"{a}.{List[a - 1]}")
    Module = ""
    while True:
        Option = input("Write the number of module(E to end):")
        if Option.isdigit():
            Option = int(Option)
            LevelList = []
            if Option <= len(module):
                # print(List[Option-1]+"1"+module[Option - 1].split(",")[0])
                for b in module:
                    if (List[Option - 1] == b.split(",")[0]):
                        LevelList.append(b.split(",")[1])
            for a, line in enumerate(LevelList, 1):
                print(f"{a}.{line}")
            while True:
                Option1 = input("Choose the level of module:")
                if Option1.isdigit():
                    Option1 = int(Option1)
                    if Option1 > 0 and Option1 < len(LevelList) + 1:
                        if Module != "":
                            Module += "+"
                        Module += (f"{List[Option - 1]}.{LevelList[Option1 - 1]}")
                        break
                    else:
                        print("Unknown Option")
        else:
            break
    return Module
def Register(Role):
    while True:
        Name = input("Name:")
        with open("namelist - profile.txt", "r") as file:
            for a in file:
                if Name == a.split(",")[0]:
                    print("This name already used!")
            if Name == a.split(",")[0]:
                continue
            break
    Password = input("Password:")
    Gmail = input("Gmail:")
    Address = input("Address:")
    ContactNumber = input("Contact Number:")
    Level = input("Level:\n1.Beginner\n2.Intermediate\n3.Advance\nChoice:")
    match Level:
        case "1":
            Level = "Beginner"
        case "2":
            Level = "Intermediate"
        case "3":
            Level = "Advance"
        case _:
            print("Unknown Option")
            return
    Module = AssignModule()
    with open("namelist - profile.txt", "a") as file:
        file.write(f"{Name},{Password},{Role},{Gmail},{ContactNumber},{Address},{Level},{Module}\n")
    print("Register Successfully")

def ViewList(Role):
    NameList = []
    with open("namelist - profile.txt", "r") as file:
        print("{:<5}|{:<20}|{:<40}|{:<20}".format("No.", "Username", "Gmail", "Moodle"))
        Number = 0
        for User in file:
            User = User.strip()
            User = User.split(",")
            if User[2] == Role:
                Number += 1
                List = [Number, User[0]]
                NameList.append(List)
                print("{:<5}|{:<20}|{:<40}|{:<20}".format(Number, User[0], User[3], User[6]))
    return NameList
def AssignLevelAndMoodle(Role):
    TrainerList = ViewList(Role)
    number = int(input("Which should be Re-Assign?\nNumber:"))
    founded = False
    line = None
    LineNum = None
    for User in TrainerList:
        if number == User[0]:
            DeletedUser = User[1]
            founded = True
            with open("namelist - profile.txt", "r") as file:
                for a, line in enumerate(file, 1):
                    line = line.split(",")
                    if line[0] == DeletedUser and line[2] == Role:
                        LineNum = a-1
                        break
            DisplayProfile(line)
    if not founded:
        print("Unknown function")
    else:
        Check = input("Wanna Change?(Y/N)")
        if Check.lower() != "y":
            print("Re-Assign Cancelled")
            return
        Level = input("Level:\n1.Beginner\n2.Intermediate\n3.Advance\nChoice:")
        match Level:
            case "1":
                Level = "Beginner"
            case "2":
                Level = "Intermediate"
            case "3":
                Level = "Advance"
            case _:
                print("Unknown Option")
                return
        Module = AssignModule()
        line[6] = Level
        line[7] = Module
        ReplaceOrDeleteLine("namelist - profile.txt", LineNum, "R", line)
        print("Re-Assign Successfully")
def Delete(Role):
    TrainerList = ViewList(Role)
    #print(TrainerList)
    if input("Wanna delete?(y/n)").lower() == "y":
        number = int(input("Which should be deleted?\nNumber:"))
        founded = False
        for User in TrainerList:
            if number == User[0]:
                DeletedUser = User[1]
                founded = True
                with open("namelist - profile.txt", "r") as file:
                    for a, line in enumerate(file, 1):
                        line = line.split(",")
                        # print(line[0],line[2])
                        if line[0] == DeletedUser and line[2] == Role:
                            DisplayProfile(line)
                            if input(f"Delete This {Role}?(Y/N)").lower() == "y":
                                print("Deleted Successfully")
                                ReplaceOrDeleteLine("namelist - profile.txt", a, "D")
                                return
                            else:
                                print("Deleted Cancelled")
                                return
    else:
        return
    if founded == False:
        print("Unknown Option")
        return
def Feedback():
    with open("Feedback.txt", "r") as file:
        print("{:<20}|{:<10}".format("Name","Content"))
        for Line in file:
            Line = Line.strip()
            Line = Line.split(",")
            print("{:<20}|{:<10}".format(Line[0],Line[1]))
    print("")

def CountStudentAmount():
    Dict = {}
    with open("student.txt","r") as file:
        for line in file:
            line = line.strip().split("|")
            module = line[6].split("+")
            for Module in module:
                if Module in Dict:
                    Dict[Module] += 1
                else:
                    Dict[Module] = 1
    return Dict
def ViewMonthlyIncomes():
    StudentDetail = CountStudentAmount()
    List=[]
    line=[]
    total = 0
    StudentNumber = 0
    for line in StudentDetail:
        num = StudentDetail[line]
        line = line.split(".")
        List.append([line[0],line[1],num])
    Select = input("Choose type of Monthly Incomes Report\n1.Trainer\n2.Level\n3.Module\nOption:")
    match Select:
        case "1":
            TrainerList = ViewList("Trainer")
            Number = int(input("Option="))
            founded = False
            for Trainer in TrainerList:
                if Number == Trainer[0]:
                    founded = True
                    Fee = []
                    with open ("Coachingclassinformation.txt","r") as file:
                        for line in file:
                            line = line.split(",")
                            if len(line) > 9:
                                line[1]+="(Additional)"
                            if line[3] == Trainer[1]:
                                count = [line[1],line[0],line[8].strip()] # add student number
                                Fee.append(count)
                    print("{:<5}{:<65}{:<15}{:<20}{:<5}|{:>15}".format("No."," Module","Level","Student Number","Fee","Total Amount"))

                    for number,content in enumerate(Fee,1):
                        for line in List:
                            if line[0] == content[0] and line[1] == content[1]:
                                StudentNumber = line[2]
                                break
                        amount = int(StudentNumber)*int(content[2])
                        total += amount
                        print("{:<5}{:<65}{:<15}{:<20}{:<5}|{:>15}".format(number, content[0], content[1],
                                                                                   StudentNumber, content[2],
                                                                                   amount))

                    print("{:>126}".format("------------"))
                    print("{:>126}".format(total))
            if not founded:
                print("Unknown Command!")
                return
            #print(TrainerList)
        case "2":
            print("1.Advance\n2.Intermediate\n3.Beginner")
            option = input("Option=")
            match option:
                case "1":
                    Lvl = "Advance"
                case "2":
                    Lvl = "Intermediate"
                case "3":
                    Lvl = "Beginner"
                case _:
                    print("Unknown Option")
                    return
            Fee = []
            with open("Coachingclassinformation.txt", "r") as file:
                for line in file:
                    line = line.split(",")
                    if len(line) > 9:
                        line[1] += "(Additional)"
                    if line[0] == Lvl:
                        count = [line[1], line[0], line[8].strip()]  # add student number
                        Fee.append(count)
            print("{:<5}{:<65}{:<15}{:<20}{:<5}|{:>15}".format("No.", " Module", "Level", "Student Number", "Fee",
                                                               "Total Amount"))
            for number, content in enumerate(Fee, 1):
                for line in List:
                    #print(line)
                    #print(content)
                    if line[0] == content[0] and line[1] == content[1]:
                        break
                amount = int(line[2]) * int(content[2])
                total += amount
                print("{:<5}{:<65}{:<15}{:<20}{:<5}|{:>15}".format(number, content[0], content[1],
                                                                   line[2], content[2],
                                                                   amount))
            print("{:>126}".format("------------"))
            print("{:>126}".format(total))
        case "3":
            module = []
            print("\nModule:")
            with open ("Coachingclassinformation.txt", "r") as file:
                for line in file:
                    line = line.split(",")
                    str = f"{line[1]}"
                    if len(line) > 9:
                        str += "(Additional)"
                    str += "," + line[0]
                    module.append(str)
            module = sorted(list(set(module)))  # all module
            Module = []
            for b in module:
                b = b.split(",")
                Module.append(b[0])
            Module = sorted(list(set(Module)))
            for a, line in enumerate(Module, 1):
                print(f"{a}.{Module[a - 1]}")
            moduleNum = int(input("Select Module:"))
            Fee = []
            with open("Coachingclassinformation.txt", "r") as file:
                for line in file:
                    line = line.split(",")
                    if len(line) > 9:
                        line[1] += "(Additional)"
                    if line[1] == Module[moduleNum-1]:
                        count = [line[1], line[0], line[8].strip()]  # add student number
                        Fee.append(count)
            print("{:<5}{:<65}{:<15}{:<20}{:<5}|{:>15}".format("No.", " Module", "Level", "Student Number", "Fee",
                                                               "Total Amount"))
            for number, content in enumerate(Fee, 1):
                for line in List:
                    if line[0] == content[0] and line[1] == content[1]:
                        break
                amount = int(line[2]) * int(content[2])
                total += amount
                print("{:<5}{:<65}{:<15}{:<20}{:<5}|{:>15}".format(number, content[0], content[1],
                                                                   line[2], content[2],
                                                                   amount))
            print("{:>126}".format("------------"))
            print("{:>126}".format(total))
        case _:
            print("Unknown Option")
            return
def Admin():
    option = input("1.Update Profile\n2.Register New Trainer\n3.View/Delete Trainer\n4.View Feedback\n5.Re-AssignTrainner\n6.View Monthly Incomes\n9.Log Out\nOption:")
    match option:
        case "1":
            UpdateProfile(UserList)
        case "2":
            Register("Trainer")
        case "3":
            Delete("Trainer")
        case "4":
            Feedback()
        case "5":
            AssignLevelAndMoodle("Trainer")
        case "6":
            ViewMonthlyIncomes()
        case "9":
            print("Log Out Successfully!\n")
            for a in range(10):
                print()
            return ("q")
        case _:
            print("Unknown Option")
            return
#Lecturer Part
def read_students():
    students = []
    with open('student.txt', 'r') as file:
        for line in file:
            student_data = line.strip().split('|')
            students.append(student_data)
    return students


def write_students(students):
    with open('student.txt', 'w') as file:
        for student in students:
            student_str = '|'.join(student) + '\n'
            file.write(student_str)


def enroll_student(students):
    name = input('Enter student name: ')
    pw = input('Enter student password:')
    tp_number = input('Enter TP number: ')
    email = input('Enter email: ')
    contact_number = input('Enter contact number: ')
    address = input('Enter address: ')
    modules = AssignModule()
    enrollment_month = input('Enter enrollment month: ')

    new_student = [name, pw, tp_number, email, contact_number, address, modules, enrollment_month]
    students.append(new_student)
    write_students(students)
    print("Student registered successfully. ")

"""
def AssignModule():
    module = []
    print("\nModule:")
    with open("Coachingclassinformation.txt", "r") as file:
        for line in file:
            line = line.split(",")
            str = f"{line[1]}"
            if len(line) > 9:
                str += "(Additional)"
            str += "," + line[0]
            module.append(str)
    module = sorted(list(set(module)))  # all module
    List = []
    for b in module:
        b = b.split(",")
        List.append(b[0])
    List = sorted(list(set(List)))
    for a, line in enumerate(List, 1):
        print(f"{a}.{List[a - 1]}")
    Module = ""
    while True:
        Option = input("Write the number of module(E to end):")
        if Option.isdigit():
            Option = int(Option)
            LevelList = []
            if Option <= len(module):
                # print(List[Option-1]+"1"+module[Option - 1].split(",")[0])
                for b in module:
                    if (List[Option - 1] == b.split(",")[0]):
                        LevelList.append(b.split(",")[1])
            for a, line in enumerate(LevelList, 1):
                print(f"{a}.{line}")
            while True:
                Option1 = input("Choose the level of module:")
                if Option1.isdigit():
                    Option1 = int(Option1)
                    if Option1 > 0 and Option1 < len(LevelList) + 1:
                        if Module != "":
                            Module += "+"
                        Module += (f"{List[Option - 1]}.{LevelList[Option1 - 1]}")
                        break
                    else:
                        print("Unknown Option")
        else:
            break
    return Module
"""

def update_student(students):
    tp_number = input('Enter the TP number of the student to update: ')
    found = False
    for i, student in enumerate(students):
        if len(student) >= 3 and student[2].strip() == tp_number:
            print(f"Student found: {student[0]} ({tp_number})")
            #print(f"Current module: {student[6]}") #correct index for modules field
            Module = student[6]
            Module = Module.split("+")
            for number,module in enumerate(Module,1):
                print("{:<5}|{:<50}".format(number,module))
            option = input("Which one should be deleted?(E to quit)")
            while option.isdigit():
                option=int(option)
                if option > 0 and option < len(Module) + 1:
                    Module.pop(option - 1)
                    for number, module in enumerate(Module, 1):
                        print("{:<5}|{:<50}".format(number, module))
                    option = input("Which one should be deleted?(E to quit)")
            print(Module)
            Module = '+'.join(Module)
            new_module = AssignModule()
            students[i][6] = Module+"+"+new_module
            print("Student information updated with the new module.")
            found = True
            break
    if not found:
        print("Student not found.")

    with open('student.txt', 'w') as file:
        for student in students:
            student_str = '|'.join(student) + '\n'
            file.write(student_str)


def get_lecturer_decision():
    decision = input("Do you approve the request? (y/n): ")
    if decision.lower() == 'y':
        return True
    elif decision.lower() == 'n':
        return False
    else:
        print("Invalid input. Please enter 'y' or 'n'. ")
        return get_lecturer_decision()


def add_module(student, module):
    student[-2] += f"+{module}"


def handle_additional_request(students):
    #tp_number = input('Enter the TP number of the student to update: ')
    Request=[]
    with open("RequestAdditionalCoachingClass.txt","r") as file:
        Number =[]
        for number,line in enumerate(file,1):
            line = line.strip().split(",")
            Request.append(line)
            if line[3] == "Pending":
                Number.append(number)
                print("{:<5}{:<20}{:<50}{:<20}{:<20}".format(number,line[0],line[1],line[2],line[3]))
        option = int(input("Which Request?"))
        if option not in Number:
            print("Unknown Request")
            return
        else:
            tp_number = Request[option-1][0]
            new_module = Request[option-1][1]
            level = Request[option-1][2]
    found = False
    for i, student in enumerate(students):
        if len(student) >= 3 and student[2].strip() == tp_number:
            print(f"Student found: {student[0]} ({tp_number})")
            print(f"Current modules: {student[6]}")
            if get_lecturer_decision():
                student[-2] += f"+{new_module}(Additional).{level}"
                print("Student information updated with the new module.")
                line[3] = "Approved"
            else:
                print("The request is rejected")
                line[3] = "Rejected"
            found = True
            break

    if not found:
        print("Student not found.")

    with open('student.txt', 'w') as file:
        for student in students:
            student_str = '|'.join(student) + '\n'
            file.write(student_str)


def delete_student(students):
    tp_number = input('Enter the TP number of the student to delete:')
    found = False
    for i, student in enumerate(students):
        if len(student) >= 3 and student[2].strip() == tp_number:
            print(f"Student found: {student[0]} ({tp_number})")
            del students[i]
            print("Student deleted successfully")
            found = True
            break
    if not found:
        print("Student not found.")

    with open('student.txt', 'w') as file:
        for student in students:
            student_str = '|'.join(student) + '\n'
            file.write(student_str)

def Lecturer():
    students = read_students()
    print("\n1. Enroll student")
    print("2. Update student information")
    print("3. Approval Additional Class")
    print("4. Delete student")
    print("5. Update profile")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        enroll_student(students)
    elif choice == 2:
        update_student(students)
    elif choice == 3:
        handle_additional_request(students)
    elif choice == 4:
        delete_student(students)
    elif choice == 5:
        UpdateProfile(UserList)
        # Add your own profile update code here
    elif choice == 9:
        print()
        return "q"
    else:
        print("Invalid choice. Please try again.")

#Trainer Part

def AddClass():
    file_path = "Coachingclassinformation.txt"
    with open(file_path) as file:
        line_list = file.readlines()
        line_list = [item.rstrip() for item in line_list]

    # Print each of the items in the list format on a new line.
    for line in line_list:
        print(line)

#Trainer Part
# Send feedback(suggestion, complain etc.)to administrator, view and exit.
def write_feedback():
    name = UserList[0]
    feedback = str(input("Enter your feedback:"))
    with open("Feedback.txt", "a") as File:
        File.seek(0, 2)
        File.write(f"{feedback},{UserList[0]}\n")
        print("Successfully submitted your feedback!")


def view_feedbacks():
    try:
        with open("Feedback.txt", "r") as file:
            feedbacks = file.readlines()

        print("Feedbacks:")
        NO = 0
        for feedback in feedbacks:
            feedback = feedback.strip().split(",")
            #print(f"{index}. {feedback[0]}")
            #print((UserList[0])+"-"+(feedback[1].strip())+"-")
            if UserList[0] == feedback[0].strip():
                NO+=1
                print(f"{NO}. {feedback[1]}")
    except FileNotFoundError:
        print("Unavailable feedbacks.")


# Add coaching class information (e.g. module name, charges, class schedule etc).
file_path = "Coachingclassinformation.txt"


def add_coaching_class_information():
    try:
        print("Add coaching class information.")
        level_name = input("Enter level name: ")
        module_name = input("Enter module name: ")
        class_code = input("Enter class code:")
        class_day = input("Enter class day: ")
        time = input("Enter the time(00:00,23:59): ")
        venue = input("Enter the venue: ")
        charges = int(input("Enter the charges: "))
        additional_coaching_class = input("Enter if it is the additional coaching class: (y/n)")
        new_information = f"{level_name},{module_name},{class_code},{UserList[0]},{class_day},{time},{venue}" \
                          f",{charges}"
        if additional_coaching_class.lower()=="y":
            new_information+=",Additional coaching class"
        new_information+="\n"
        with open("Coachingclassinformation.txt", "a") as file:
            file.write(new_information)
        with open("namelist - profile.txt","r") as file:
            for number,line in enumerate(file,1):
                line=line.split(",")
                if line[0] == UserList[0]:
                    module=line[7]
                    module+=f"+{module_name}"
                    if additional_coaching_class.lower()=="y":
                        module+="(Additional)"
                    module+=f".{level_name}"
                    line[7]=module
                    line[-1]=line[-1].replace('\n', '')
                    ReplaceOrDeleteLine("namelist - profile.txt",number-1,"R",line)
        print("Coaching class information added successfully.")
    except ValueError as ve:
        print(f"Error: {ve}. Please enter a valid numeric value for time and charges.")

#add_coaching_class_information()

# To update coaching class information.


def update_coaching_class_information():
    try:
        # Read the current information.
        with open("Coachingclassinformation.txt", "r") as file:
            lines = file.readlines()

        # Display the current information.
        print("Existing coaching class information:")
        lineNumber = []
        for index, line in enumerate(lines, start=1):
            module = line.split(",")
            if module[3] == UserList[0]:
                lineNumber.append(index)
                print(f"{index}. {line.strip()}")

        # Select the information to update.
        line_number = int(input("Enter the line number to update: "))
        if line_number in lineNumber:
            updated_level_name = input("Enter the updated level name: ")
            updated_module_name = input("Enter the updated module name: ")
            updated_class_code = input("Enter class code:")
            updated_class_day = input("Enter the updated class day: ")
            updated_time = input("Enter the updated time(00:00,23:59): ")
            updated_venue = input("Enter the updated venue: ")
            updated_charges = int(input("Enter the updated charges: "))
            additional_coaching_class = input("Enter if it is the additional coaching class: (y/n)")



            # Update the chosen line.
            lines[line_number - 1] = f"{updated_level_name},"\
                                     f"{updated_module_name}," \
                                     f"{updated_class_code}," \
                                     f"{UserList[0]},"\
                                     f"{updated_class_day},"\
                                     f"{updated_time},"\
                                     f"{updated_venue},"\
                                     f"{updated_charges}"
            if additional_coaching_class.lower() == "y":
                lines[line_number - 1] += ",Additional coaching class"
                lines[line_number - 1] += "\n"

            # Write the updated information back to the text file.
            with open("Coachingclassinformation.txt", "w") as file:
                file.writelines(lines)

            print("Coaching class information updated successfully!")
        else:
            print("Invalid line number!")
    except ValueError:
        print("Invalid input! Please enter a number.")

# To delete coaching class information.


def delete_coaching_class_information():
    try:
        # Read the current information.
        with open("Coachingclassinformation.txt", "r") as file:
            lines = file.readlines()

        # Display the current information.
        print("Existing Coaching Class Information:")
        lineNumber=[]
        for index, line in enumerate(lines, start=1):
            module = line.split(",")
            if module[3] == UserList[0]:
                lineNumber.append(index)
                print(f"{index}. {line.strip()}")

        # Select the information to delete.
        line_number = int(input("Enter the line number to delete: "))
        print(lineNumber)
        if line_number in lineNumber:
            # Remove the chosen line.
            lines.pop(line_number - 1)

            # Write the modified lines back to the text file.
            with open("Coachingclassinformation.txt", "w") as file:
                file.writelines(lines)

            print("Coaching class information deleted successfully!")
        else:
            print("Invalid line number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


# Options to update and delete.

# View list of students enrolled and paid for his/her modules.
def ViewStudentPaymentStatus():
    file_path = "Coachingclassinformation.txt"
    with open(file_path) as file:
        line_list = file.readlines()
        line_list = [item.rstrip() for item in line_list]

        # Print each of the items in the list format on a new line.
        for line in line_list:
            print(line)

    while True:
        print("\n1. View list students enrolled and paid for his/her modules.")
        print("2. Exit.")

        option = input("Enter your option (1 or 2): ")
        if option == "1":
            write_feedback()
        elif option == "2":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please enter 1 or 2.")
def Trainer():
    option = input("1.Write feedback.\n2.view feedback.\n3.Add coaching class information.\n4.Update coaching class information.\n5.Delete coaching class information.\n6.Update Profile.")
    match option:
        case "1":
            write_feedback()
        case "2":
            view_feedbacks()
        case"3":
            add_coaching_class_information()
        case "4":
            update_coaching_class_information()
        case"5":
            delete_coaching_class_information()
        case "6":
            UpdateProfile(UserList)
#student part
def display_menu():
    print("\nMenu:")
    print("1. View Schedule")
    print("2. Send Request to Enroll in Additional Class")
    print("3. Delete Request")
    print("4. View Invoices")
    print("5. Make Payment")
    print("6. Update Profile")
    print("0. Exit")


def view_schedule():
    print(f"Schedule for this work")
    day = input("Enter day you want to check schedule for: ").capitalize()
    level = input("Enter your level: ").capitalize()
    print("Your schedule")
    with open("Coachingclassinformation.txt", "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        data = line.strip().split(",")

        if data[4] == day and data[0] == level:
            print(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}, {data[6]}, {data[7]}")


def send_request():
    try:
        tp_number = input("Enter TP Number: ")
        module = input("Enter Module: ")
        level = input("Enter Level: ")

        with open("RequestAdditionalCoachingClass.txt", 'a') as file:
            file.write(f"{tp_number},{module},{level},Pending\n")

        print("Request sent successfully.")
    except Exception as e:
        print(f"An error occurred while sending the request: {e}")


def delete_request():
    try:
        # Print the existing requests before asking for deletion
        print("Existing requests:")
        with open("RequestAdditionalCoachingClass.txt", 'r') as file:
            print(file.read())

        tp_number = input("Enter TP Number to delete request: ")
        module = input("Enter Module to delete request: ")
        level = input("Enter Level to delete request: ")

        with open("RequestAdditionalCoachingClass.txt", 'r') as file:
            lines = file.readlines()

        with open("RequestAdditionalCoachingClass.txt", 'w') as file:
            for line in lines:
                if f"{tp_number},{module},{level}" not in line:
                    file.write(line)

        print("Request deleted successfully.")
    except Exception as e:
        print(f"An error occurred while deleting the request: {e}")


def create_invoice():
    try:
        # Read the content of Coachingclassinformation.txt
        with open("Coachingclassinformation.txt", "r") as file:
            lines = file.readlines()

        print("Available Modules:")
        for line in lines:
            # Splitting the line into fields
            fields = line.strip().split(', ')
            module_name = fields[1]
            level = fields[0]
            price = fields[-1]

            # Printing module name and level
            print(f"Module: {module_name}, Level: {level}, Price: {price}")

        # Input TP Number, Module Name, and Level
        tp_number = input("Enter TP Number: ")
        module_name = input("Enter Module Name: ")
        level = input("Enter Level: ")

        # Find the price for the given module and level
        found = False
        for line in lines:
            fields = line.strip().split(', ')
            if fields[0] == level and fields[1] == module_name:
                price = fields[-1]
                found = True
                break

        if found:
            # Write the invoice to Invoice.txt
            with open("Invoice.txt", "a") as file:
                file.write(f"TP Number: {tp_number}, Module: {module_name}, Level: {level}, Price: {price}\n")
            print("Invoice created successfully.")
        else:
            print("Module name and level not found.")
    except FileNotFoundError:
        print("Coachingclassinformation.txt not found.")


def make_payment():
    try:
        # Read the content of Invoice.txt
        with open("Invoice.txt", "r") as file:
            invoices = file.readlines()

        # Input TP Number
        tp_number = input("Enter TP Number: ")

        # Find the invoice for the given TP Number
        found = False
        for invoice in invoices:
            if f"TP Number: {tp_number}" in invoice:
                found = True
                print("Invoice:")
                print(invoice)

                # Ask if the user wants to make the payment now
                choice = input("Do you want to make the payment now? (yes/no): ")
                if choice.lower() == "yes":
                    # Extract invoice details
                    details = invoice.strip().split(", ")
                    module_name = details[1].split(": ")[1]
                    level = details[2].split(": ")[1]
                    price = details[3].split(": ")[1]

                    # Write payment details to Payment.txt
                    with open("Payment.txt", "a") as payment_file:
                        payment_file.write(
                            f"TP Number: {tp_number}, Module: {module_name}, Level: {level}, Price: {price}, Payment Received: yes\n")
                    print("Payment received and invoice updated.")
                elif choice.lower() == "no":
                    print("Payment postponed.")
                else:
                    print("Invalid choice.")
                break

        if not found:
            print("Invoice not found for the provided TP Number.")
    except FileNotFoundError:
        print("Invoice.txt not found.")


# Rest of the code remains the same

def Student():
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        # Implement view schedule functionality
        view_schedule()
    elif choice == "2":
        send_request()
    elif choice == "3":
        delete_request()
    elif choice == "4":
        # Implement view invoices functionality
        create_invoice()
    elif choice == "5":
        # Implement make payment functionality
        make_payment()
    elif choice == "6":
        # Implement update profile functionality
        UpdateProfile(UserList)
    elif choice == "0":
        print("Exiting...")
        return "q"
    else:
        print("Invalid choice. Please enter a number from the menu.")

while True:
    UserList = Login()
    while True:
        status = UserProfile(UserList)
        if status == "Admin":
            if Admin() == "q":
                break
        if status == "Lecturer":
            if Lecturer() == "q":
                break
        if status == "Trainer":
            if Trainer() == "q":
                break
        if status == "Student":
            if Student() == "q":
                break

#print(User)
#Register("Admin")s