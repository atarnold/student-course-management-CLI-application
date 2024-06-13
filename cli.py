from tabulate import tabulate
from models import Student, Course, Enrollment, session

class CLI:
    def run(self):
        while True:
            choice = input("Choose an option:\n1. Add Student\n2. Add Course\n3. Enroll Student\n4. List Students\n5. List Courses\n6. List Enrollments\n7. Exit\n")
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.add_course()
            elif choice == '3':
                self.enroll_student()
            elif choice == '4':
                self.list_students()
            elif choice == '5':
                self.list_courses()
            elif choice == '6':
                self.list_enrollments()
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")

    def add_student(self):
        name = input("Enter student name: ")
        student = Student(name=name)
        session.add(student)
        session.commit()
        print("Student added successfully.")

    def add_course(self):
        title = input("Enter course title: ")
        course = Course(title=title)
        session.add(course)
        session.commit()
        print("Course added successfully.")

    def enroll_student(self):
        student_id = int(input("Enter student id: "))
        course_id = int(input("Enter course id: "))
        grade = input("Enter grade (optional): ")
        enrollment = Enrollment(student_id=student_id, course_id=course_id, grade=grade)
        session.add(enrollment)
        session.commit()
        print("Student enrolled successfully.")

    def list_students(self):
        students = session.query(Student).all()
        table = [[student.id, student.name] for student in students]
        print(tabulate(table, headers=["ID", "Name"]))

    def list_courses(self):
        courses = session.query(Course).all()
        table = [[course.id, course.title] for course in courses]
        print(tabulate(table, headers=["ID", "Title"]))

    def list_enrollments(self):
        enrollments = session.query(Enrollment).all()
        table = [[enrollment.student_id, enrollment.course_id, enrollment.grade] for enrollment in enrollments]
        print(tabulate(table, headers=["Student ID", "Course ID", "Grade"]))

if __name__ == "__main__":
    CLI().run()
