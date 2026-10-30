# student grade management system using oops (concept of classes and objects): 

class Student: 
    def __init__(self, name, maths, python, electronics, chemistry, datascience ):
         self.name = name 
         self.maths = maths 
         self.python = python 
         self.electronics = electronics
         self.chemistry = chemistry  
         self.datascience = datascience
         
    def calculate_percentage(self): 
        total = (self.maths + self.python + self.electronics + self.chemistry 
                 + self.datascience) 
        
        percentage = total/5
        return percentage
    
    def calculate_grade(self): 
        percentage = self.calculate_percentage() 
        
        if percentage >= 90: 
            return "A+"
        elif percentage >= 80: 
            return "A"
        elif percentage >=70: 
            return "B"
        elif percentage >= 60: 
            return "C"
        elif percentage >= 50: 
            return "D"
        elif percentage >= 45: 
            return "E"
        else: 
            return "F"
        
    def display_result(self): 
        total = (self.maths + self.python + self.electronics + self.chemistry 
                + self.datascience)
        
        print("\n ---------- STUDENT RESULT ----------")
        print("NAME : ", self.name) 
        print("TOTAL MARKS : ", total, "/500")
        print(f"PERCENTAGE : {self.calculate_percentage():.2f}%")
        print("GRADE : ", self.calculate_grade())
        
       
        
           
    def suggest_improvement(self):
        print("\n--- Subject Improvement Analysis ---")

        # Store subject names and their marks
        subjects = {
            "Maths": self.maths,
            "Python": self.python,
            "Electronics": self.electronics,
            "Chemistry": self.chemistry,
            "Datascience": self.datascience
        }

        # Find the subject with the lowest marks
        lowest_subject = min(subjects, key=subjects.get)
        lowest_marks = subjects[lowest_subject]

        print(f"Lowest Marks: {lowest_subject} ({lowest_marks}/100)")
        print(f"You need to focus more on {lowest_subject}.")

        # Give suggestions based on marks
        for subject, marks in subjects.items():
               if marks < 40:
                   print(f"{subject}: You need major improvement. Revise the basics and practise daily.")
               elif marks < 60:
                print(f"{subject}: Your performance needs improvement. Solve more practice questions.")
               elif marks < 75:
                print(f"{subject}: Good effort! More revision can improve your marks.")
        else:
                print(f"{subject}: Good performance! Keep it up.")

student1 = Student("Amaan", 95, 92, 89, 91, 97)
student2 = Student("Yafis", 91, 85, 78, 90, 99)
student3 = Student("Musiab", 89, 87, 81, 79, 100)
student4 = Student("Huzaif", 91, 76, 41, 0, 100)
student5 = Student("Mariyah", 92, 97, 78, 90, 97)
student6 = Student("Saasha", 89, 99, 100, 97, 91)
student7 = Student("Kafeel", 90, 61, 89, 100, 72)
student8 = Student("Osama", 55, 90, 71, 89, 99)
student9 = Student("Manzoor", 90, 99, 19, 71, 66)
student10 = Student("Payaam", 66, 78, 91, 55, 100)
student1.display_result() 
student1.suggest_improvement()
student2.display_result()
student2.suggest_improvement()
student3.display_result()
student3.suggest_improvement()
student4.display_result()
student4.suggest_improvement()
student5.display_result()
student5.suggest_improvement()
student6.display_result()
student6.suggest_improvement()
student7.display_result()
student7.suggest_improvement()
student8.display_result()
student8.suggest_improvement()
print("------------------------------------")           
        
        