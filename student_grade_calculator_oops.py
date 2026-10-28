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
        
student1 = Student("Amaan", 95, 92, 89, 91, 97)
student1.display_result()        
        
           
           