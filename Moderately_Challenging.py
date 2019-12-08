class Person:
    def __init__(self, name, address):
        self.name = str(name)
        self.address = str(address)
    def getName(self):
        print(self.name)
    def getAddress(self):
        print(self.address)
    def setAddress(self):
        self.name = input("Please input the name: ")
    #def toString(self):
        #Again, not sure what it's supposed to do.
class Student(Person):
    def __init__(self, numCourses, courses, grades, name, address):
        super().__init__(name, address)
        self.numCourses = int(numCourses)
        self.courses = str(courses[{}])
        self.grades = int(grades[{}])
    #def addCourseGrade(self, course, grade):
    #I'm lost, I'm not sure what it wants me to do anymore lol
class Teacher(Person):
    def __init__(self, numCourses, courses, name, address):
        super().__init__(name, address)
        self.numCourses = numCourses
        self.courses = courses[{}]
    #def addCourse(self):