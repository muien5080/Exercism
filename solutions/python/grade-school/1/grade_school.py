class School:
    def __init__(self):
        # Dictionary mapping grade -> list of student names
        self.students_by_grade = {}
        # Set to track all student names globally to avoid duplicates
        self.all_students = set()
        # Keep track of last add_student results for `added()`
        self.last_add_results = []

    def add_student(self, name, grade):
        # Check if student is already in the school
        if name in self.all_students:
            self.last_add_results.append(False)
            return False

        # Add grade if it doesn't exist
        if grade not in self.students_by_grade:
            self.students_by_grade[grade] = []

        # Add student
        self.students_by_grade[grade].append(name)
        self.all_students.add(name)
        self.last_add_results.append(True)
        return True

    def grade(self, grade_number):
        # Return a sorted list of students in that grade
        if grade_number not in self.students_by_grade:
            return []
        return sorted(self.students_by_grade[grade_number])

    def roster(self):
        # Return all students sorted by grade and alphabetically
        all_students_sorted = []
        for grade in sorted(self.students_by_grade.keys()):
            all_students_sorted.extend(sorted(self.students_by_grade[grade]))
        return all_students_sorted

    def added(self):
        # Return the list of booleans from last add_student calls
        return self.last_add_results