students = []


with open('student.csv', 'w') as file:
    file.write("""name,branch,gpa
Rahul,CSE-DS,8.5
Sneha,ECE,6.2
Anish,CSE-DS,9.1
Priya,CSE,7.8
""")




try:
    with open('student.csv', 'r') as file:
        header = file.readline()


        for line in file:
            data = line.strip().split(',')


            name = data[0]
            branch = data[1]
            CGPA = float(data[2])

            if branch == "CSE-DS" and CGPA >= 8.0:
                students.append(name)
                print(f"--> Match found! Adding {name}")  

    with open("eligible_students.txt", "w") as output_file:
        for student in students:
            output_file.write(f"{student}\n")


    print("data processing")


except FileNotFoundError:
    print("The student file does not exist")