class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and I study {self.course}.")

student1 = Student("Nacar,Joana Rose M.", 20, "INFORMATION TECHNOLOGY")
student2 = Student("Obello,Trishia A.", 22, "INFORMATION TECHNOLOGY")
student3 = Student("Mercolita Meann", 23, "INFORMATION TECHNOLOGY")

student1.introduce()
student2.introduce()
student3.introduce()