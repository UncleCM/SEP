class University():
    def __init__(self, universityName):
        self.universityName = universityName
        
class Course:
    def __init__(self, credit, id, lecturer, name, semester):
        self.credit = credit
        self.id = id
        self.lecturer = lecturer
        self.name = name
        self.semester = semester
        self.students = []

    def enroll(self, student_name):
        self.students.append(student_name)
        return
    
    def getCredit(self):
        return self.credit
    
    def getLecturer(self):
        return self.lecturer
    
    def getStudents(self):
        return self.students

class Lecturer:
    def __init__(self, name):
        self.name = name

    def getCourses(self):
        return self.name

class Program:
    def __init__(self, name, level, start):
        self.name = name
        self.level = level
        self.start = start

    def addCourse(self, course):
        self.courses.append(course)

    def getCourse(self):
        return []

class Student:
    def __init__(self, name):
        self.name = name
        self.status = "normal"

class Takes:
    def __init__(self, grade, score):
        self.grade = grade
        self.score = score

class Transcript:
    def __init__(self, takes, complete, issueDate):
        self.takes = takes
        self.complete = complete
        self.issueDate = issueDate

    def printTranscript(self):
        print(f"Grade: {self.takes.grade}")
        print(f"Score: {self.takes.score}")
        print(f"Complete: {self.complete}")
        print(f"Issue Date: {self.issueDate}")
