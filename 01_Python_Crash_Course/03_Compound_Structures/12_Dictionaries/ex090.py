# Exercise 090 - Python Dictionary

"""Make a program that reads a student's name and average, also storing the 
situation in a dictionary. At the end, show the content of the structure on the screen."""

student_info = dict()
condition = ""

name = str(input("Enter the students name: "))
student_avg = float(input(f"Enter {name} average grade: "))

student_info["name"] = name
student_info["mean"] = student_avg

print(f"The students name is: {name}")
print(f"And his grade is: {student_avg}")

if student_avg >= 7:
    condition = "Approved!"
elif 5 < student_avg < 7:
    condition = "Recovery!"
else:
    condition = "disapproved!"

print(f"He's been {condition}")
