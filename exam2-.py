#1 Different methods for reading from a file:
# f.read() / f.readlines() / f.readline()
#2
"""
def sort_dict(d):
    return sorted(d.values(), key=d.get)
"""
#3
"""
with open("file.txt", "r") as f:
    for line in f:
        with open("file2.txt", "w") as f2:
            f2.write(line + "\n")  # Corrected the write method
"""
# Problem:
#1
def input_data():
    d = {}
    while True:
        user_input = input("Enter 'no' or 'NO' to quit, or 'yes' to continue: ").lower()
        if user_input == "yes":
            n = int(input("Enter the number of trainees: "))
            trainee_id = input("Enter the trainee's ID: ")
            for _ in range(n):  # Using '_' as a temporary variable
                last_name = input("Enter the trainee's last name: ")
                first_name = input("Enter the trainee's first name: ")
                grades = []
                for _ in range(n): 
                    grade = float(input("Enter the trainee's grade: "))
                    grades.append(grade)
                major = input("Enter the trainee's major: ")
                t = (last_name, first_name, grades, major)
                d[trainee_id] = t
            return d
        elif user_input == "no":
            break

#2
def display(d):
    for i, j in d.items():
        print(f"Trainee information {i}:\nID => {i}")
        print(f"Last Name => {j[0]}\nFirst Name => {j[1]}\nGrades => {j[2]}\nMajor => {j[3]}\n")

def search(d, num):
    if num in d:
        last_name = d[num][0]
        first_name = d[num][1]
        full_name = last_name + " " + first_name 
        return full_name
    else:
        print("The trainee ID does not exist.")

def delete(d, num):
    if num in d:
        d.pop(num)
        print("Deletion was successful.")
    else:
        print("Invalid ID")

def top_trainee(d):
    d_p = {}
    for i, j in d.items():
        total = sum(j[2])
        average = total / len(j[2])
        d_p[i] = average

    return max(d_p, key=d_p.get)

def save(d):
    with open("trainees.txt", "w") as f:
        for i, j in d.items():
            total = sum(j[2])
            average = total / len(j[2])
            f.write(f"Trainee => ID: {i}, Last Name: {j[0]}, First Name: {j[1]}, Average: {average}, Major: {j[3]}\n")

# Main Program:
d = {}
while True:
    choice = input("""--------------------------MENU-------------------------------
1-Input trainees
2-Display trainees
3-Delete trainees
4-Save trainees
5-Top trainee
6-Quit
Enter your choice: """)
    if choice == "1":
        d = input_data()
    elif choice == "2":
        display(d)
    elif choice == "3":
        num = input("Enter the ID to delete a trainee: ")
        delete(d, num)
    elif choice == "4":
        save(d)
        print("Save was successful.")
    elif choice == "5":
        print(f"The top trainee is {top_trainee(d)}")
    elif choice == "6":
        print("End of Program")
        break
    else:
        print("Invalid choice")
