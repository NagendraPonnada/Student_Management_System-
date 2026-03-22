import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management_system.settings')
django.setup()

from testapp.models import Student

def get_all_students():
    """Get all students"""
    students = Student.objects.all()
    return students

def get_active_students():
    """Get only active students"""
    students = Student.objects.filter(is_active=True)
    return students

def get_student_by_enrollment(enrollment_number):
    """Get student by enrollment number"""
    try:
        student = Student.objects.get(enrollment_number=enrollment_number)
        return student
    except Student.DoesNotExist:
        return None

def get_students_by_city(city):
    """Get students by city"""
    students = Student.objects.filter(city__icontains=city)
    return students

def search_students(search_term):
    """Search students by name, enrollment, or email"""
    students = Student.objects.filter(
        models.Q(enrollment_number__icontains=search_term) |
        models.Q(first_name__icontains=search_term) |
        models.Q(last_name__icontains=search_term) |
        models.Q(email__icontains=search_term)
    )
    return students

# Example usage
if __name__ == "__main__":
    from django.db import models

    print("=== All Students ===")
    for student in get_all_students():
        print(f"{student.enrollment_number}: {student.get_full_name()}")

    print("\n=== Active Students ===")
    for student in get_active_students():
        print(f"{student.enrollment_number}: {student.get_full_name()}")

    print("\n=== Search by Enrollment ===")
    student = get_student_by_enrollment("20J21A0565")
    if student:
        print(f"Found: {student.get_full_name()}")
    else:
        print("Student not found")

    print("\n=== Students by City ===")
    for student in get_students_by_city("Hyderabad"):
        print(f"{student.enrollment_number}: {student.get_full_name()}")

    print("\n=== Search Students ===")
    for student in search_students("Nagendra"):
        print(f"{student.enrollment_number}: {student.get_full_name()}")