# Name: Georgia Vrana
# Date Submitted: Tuesday, March 26th, 2024
# Assignment-7: Student Data
# Description: The code defines a `Student` class with attributes for student details, 
#              initializes a list of student objects with provided data, and prints each
#              student's information in a specified format.

# Define the Student class with initialization method that accepts all required attributes.
class Student:
    # The __init__ method sets up the object with default values for gender and current_avg if not provided.
    def __init__(self, student_number, first_name, last_name, year_enrolled, gender='Not set', current_avg=0):
        self.student_number = student_number  # Unique identifier for the student
        self.first_name = first_name  # First name of the student
        self.last_name = last_name  # Last name of the student
        self.year_enrolled = year_enrolled  # The year the student enrolled
        self.gender = gender  # Gender of the student, default is 'Not set'
        self.current_avg = current_avg  # Current average grade, default is 0
    
    # String representation method for printing student details in a specific format.
    def __str__(self):
        return (f"{self.first_name} {self.last_name}, student number {self.student_number}, "
                f"has a gender of {self.gender.lower()} was enrolled in {self.year_enrolled} "
                f"and has a current average of {self.current_avg}")

# Data for 5 students as a list of tuples. Each tuple contains all the information for a student.
students_data = [
    ("001", "Mickey", "Mouse", 1932, "M", 64),
    ("002", "Minnie", "Poppins", 1914, "F", 94),
    ("003", "Charlie", "Chaplin", 1928, "M", 55),
    ("004", "Willy", "Wonka", 1949, "M", 84),
    ("005", "Shirley", "Temple", 1936, "F", 72)
]

# Create a list to store the instantiated Student objects.
students = []
for data in students_data:
    # Create a Student object with data unpacked from the tuple, except gender and current_avg.
    student = Student(*data[:-2])  # Pass only the required arguments for instantiation
    student.gender = data[-2]  # Set gender from the tuple
    student.current_avg = data[-1]  # Set current average grade from the tuple
    students.append(student)  # Add the student object to the list

# Print the details of each student in the specified format.
for student in students:
    print(student)



