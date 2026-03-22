import os
import django
import pymysql

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management_system.settings')
django.setup()

from testapp.models import Student

def demonstrate_crud():
    """Demonstrate all CRUD operations"""
    print("🎓 STUDENT MANAGEMENT SYSTEM - CRUD OPERATIONS DEMO")
    print("=" * 60)

    # CREATE - Add new student
    print("\n📝 CREATE: Adding a new student...")
    try:
        new_student = Student.objects.create(
            enrollment_number='24J21A0001',
            first_name='Emma',
            last_name='Watson',
            email='emma.watson@example.com',
            phone='9876543220',
            date_of_birth='2003-04-15',
            gender='F',
            address='567 Oak Street, Apt 4B',
            city='Ahmedabad',
            state='Gujarat',
            zipcode='380001'
        )
        print(f"✅ Created: {new_student.get_full_name()} (ID: {new_student.id})")
    except Exception as e:
        print(f"❌ Create failed: {e}")

    # READ - Retrieve students
    print("\n📖 READ: Retrieving student data...")

    # Get all students
    all_students = Student.objects.all()
    print(f"📊 Total students: {all_students.count()}")

    # Get specific student
    try:
        student = Student.objects.get(enrollment_number='24J21A0001')
        print(f"🎯 Found student: {student.get_full_name()} from {student.city}")
    except Student.DoesNotExist:
        print("❌ Student not found")

    # Filter students
    active_students = Student.objects.filter(is_active=True)
    print(f"✅ Active students: {active_students.count()}")

    # UPDATE - Modify student data
    print("\n✏️ UPDATE: Modifying student information...")
    try:
        student = Student.objects.get(enrollment_number='24J21A0001')
        old_phone = student.phone
        student.phone = '9876543221'  # Update phone number
        student.city = 'Surat'  # Update city
        student.save()
        print(f"✅ Updated {student.get_full_name()}: Phone {old_phone} → {student.phone}, City → {student.city}")
    except Exception as e:
        print(f"❌ Update failed: {e}")

    # DELETE - Remove student
    print("\n🗑️ DELETE: Removing a student...")
    try:
        student = Student.objects.get(enrollment_number='24J21A0001')
        name = student.get_full_name()
        student.delete()
        print(f"✅ Deleted student: {name}")
    except Exception as e:
        print(f"❌ Delete failed: {e}")

    # Final count
    final_count = Student.objects.count()
    print(f"\n📈 Final student count: {final_count}")

def mysql_crud_demo():
    """Demonstrate CRUD operations directly in MySQL"""
    print("\n" + "=" * 60)
    print("🗄️ MYSQL DIRECT CRUD OPERATIONS")
    print("=" * 60)

    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='student_management_system'
        )
        cursor = conn.cursor()

        # CREATE
        print("\n📝 MySQL CREATE: Adding student...")
        insert_query = """
        INSERT INTO testapp_student
        (enrollment_number, first_name, last_name, email, phone, date_of_birth,
         gender, address, city, state, zipcode, joining_date, is_active, created_at, updated_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURDATE(), 1, NOW(), NOW())
        """
        cursor.execute(insert_query, ('24J21A0002', 'Michael', 'Jordan', 'michael@example.com',
                                    '9876543222', '2003-02-17', 'M', 'Basketball Court 23',
                                    'Jaipur', 'Rajasthan', '302001'))
        conn.commit()
        print("✅ MySQL: Student created")

        # READ
        print("\n📖 MySQL READ: Retrieving data...")
        cursor.execute("SELECT COUNT(*) FROM testapp_student")
        count = cursor.fetchone()[0]
        print(f"📊 MySQL: Total students = {count}")

        cursor.execute("SELECT enrollment_number, first_name, last_name, city FROM testapp_student WHERE enrollment_number = '24J21A0002'")
        student = cursor.fetchone()
        if student:
            print(f"🎯 MySQL: Found {student[1]} {student[2]} from {student[3]}")

        # UPDATE
        print("\n✏️ MySQL UPDATE: Modifying data...")
        cursor.execute("UPDATE testapp_student SET phone = '9876543223' WHERE enrollment_number = '24J21A0002'")
        conn.commit()
        print("✅ MySQL: Phone number updated")

        # DELETE
        print("\n🗑️ MySQL DELETE: Removing data...")
        cursor.execute("DELETE FROM testapp_student WHERE enrollment_number = '24J21A0002'")
        conn.commit()
        print("✅ MySQL: Student deleted")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"❌ MySQL Error: {e}")

if __name__ == "__main__":
    # Django ORM CRUD
    demonstrate_crud()

    # MySQL Direct CRUD
    mysql_crud_demo()

    print("\n" + "=" * 60)
    print("🎉 CRUD OPERATIONS DEMO COMPLETED!")
    print("🌐 Web Interface: http://127.0.0.1:8000/")
    print("🔧 Admin Panel: http://127.0.0.1:8000/admin/")
    print("=" * 60)