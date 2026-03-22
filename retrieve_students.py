import os
import django
import pymysql

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management_system.settings')
django.setup()

from testapp.models import Student

def retrieve_students():
    """Retrieve all students using Django ORM"""
    print("=== Retrieving Students using Django ORM ===\n")

    # Get all students
    students = Student.objects.all()

    if not students:
        print("No students found in the database.")
        return

    print(f"Total students: {students.count()}\n")

    for student in students:
        print(f"ID: {student.id}")
        print(f"Enrollment: {student.enrollment_number}")
        print(f"Name: {student.get_full_name()}")
        print(f"Email: {student.email}")
        print(f"Phone: {student.phone}")
        print(f"City: {student.city}")
        print(f"Active: {student.is_active}")
        print(f"Joining Date: {student.joining_date}")
        print("-" * 50)

def retrieve_students_mysql():
    """Retrieve students directly from MySQL"""
    print("\n=== Retrieving Students directly from MySQL ===\n")

    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='student_management_system'
        )

        cursor = conn.cursor()

        # Query to get all students
        cursor.execute("SELECT id, enrollment_number, first_name, last_name, email, phone, city, is_active, joining_date FROM testapp_student")

        students = cursor.fetchall()

        if not students:
            print("No students found in the database.")
        else:
            print(f"Total students: {len(students)}\n")

            for student in students:
                print(f"ID: {student[0]}")
                print(f"Enrollment: {student[1]}")
                print(f"Name: {student[2]} {student[3]}")
                print(f"Email: {student[4]}")
                print(f"Phone: {student[5]}")
                print(f"City: {student[6]}")
                print(f"Active: {'Yes' if student[7] else 'No'}")
                print(f"Joining Date: {student[8]}")
                print("-" * 50)

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error connecting to database: {e}")

if __name__ == "__main__":
    retrieve_students()
    retrieve_students_mysql()