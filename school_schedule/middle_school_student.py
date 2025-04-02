from .student import Student

# add MiddleSchoolStudent here
class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation = True):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation

    def summary(self):
        student_summary = super().summary()
        
        if not self.gets_transportation:
            student_summary += ", doesn't get transportation."
        else:
            student_summary += ", get's transportation."
        
        return student_summary
