print("======================================================")
print("===========================STUDENT GRADE CALCULATOR===========================")
name = input("ENTER STUDENT'S NAME: ")

maths = float(input("ENTER MATHS MARKS(out of 100): "))
python = float(input("ENTER PYTHON MARKS(out of 100): "))
electonics = float(input("ENTER ELECTRONICS MARKS(out of 100): "))
eng_chemistry = float(input("ENTER ENGINEERING CHEMISTRY MARKS(out of 100): "))
data_sciences = float(input("ENTER DATA SCIENCES MARKS(out of 100): "))

total = maths + python + electonics + eng_chemistry + data_sciences
percentage = total/5

if percentage >= 90:
    grade = 'A+'
elif percentage >=80: 
    grade = 'A'
elif percentage >= 70: 
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >=50: 
    grade = 'D'
elif percentage >=45: 
    grade = "E"
else: 
    grade = "F"
    

print("===========================RESULT===========================") 
print("STUDENTS NAME: ", name)
print("TOTAL MARKS: ", total, "/500")
print(f"PERCENTAGE: {percentage:.2f}%")
print("GRDAE: ", grade)

if percentage >= 45: 
    print("STATUS: PASS ")
else: 
    print("STATUS : FAIL ") 
 
print("=======================================================")                     