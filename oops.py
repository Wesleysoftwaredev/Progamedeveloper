class student:
    def __init__(self, name, age, grade, houseteams, iq, teacher):
        self.name=name
        self.age=age
        self.grade=grade
        self.houseteams=houseteams
        self.iq=iq
        self.teacher=teacher
        self.school="canon slade"
        self.principal="mr gilhooly"
        self.uniformcolor="green"
    def display(self):
        print(f"name of student is {self.name}")
        print(f"age of student is {self.age}")
        print(f"grade of student is {self.grade}")
        print(f"houseteams of student is {self.houseteams}")
        print(f"iq of student is {self.iq}")
        print(f"teacher of student is {self.teacher}")
        print(f"school of student is {self.school}")
        print(f"principal of student is {self.principal}")
        print(f"uniformcolor of student is {self.uniformcolor}")
s1 = student("christopher", "16", "year 11", "mandela", "120", "mrs childs")
s1.principal="mr brunsden"
s1.display()