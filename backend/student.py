class Student:
    def __init__(self, first_name, last_name, student_class, student_id, parent_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_class = student_class
        self.student_id = student_id
        self.parent_id = parent_id

    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def schoolinfo(self):
        return '{}{}'.format(self.student_id, self.student_class)

    def __repr__(self):
        return "Student ('{}', '{}'), '{}'".format(self.first_name, self.last_name, self.student_class)
