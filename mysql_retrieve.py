import pymysql

def connect_mysql():
    """Connect to MySQL database"""
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='student_management_system'
        )
        return conn
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return None

def retrieve_all_students():
    """Retrieve all students from testapp_student table"""
    conn = connect_mysql()
    if not conn:
        return

    try:
        cursor = conn.cursor()

        # Get all students
        cursor.execute("SELECT * FROM testapp_student")
        students = cursor.fetchall()

        print("=== ALL STUDENTS FROM MYSQL DATABASE ===\n")
        print(f"Total students found: {len(students)}\n")

        if not students:
            print("No students found in the database.")
            return

        # Display column headers
        print("┌" + "─" * 150 + "┐")
        print("│ {:<3} │ {:<15} │ {:<15} │ {:<15} │ {:<25} │ {:<12} │ {:<10} │ {:<8} │ {:<10} │".format(
            "ID", "Enrollment", "First Name", "Last Name", "Email", "Phone", "City", "Active", "Join Date"
        ))
        print("├" + "─" * 150 + "┤")

        # Display student data
        for student in students:
            active_status = "Yes" if student[13] else "No"  # is_active field
            print("│ {:<3} │ {:<15} │ {:<15} │ {:<15} │ {:<25} │ {:<12} │ {:<10} │ {:<8} │ {:<10} │".format(
                student[0],  # id
                student[1],  # enrollment_number
                student[2],  # first_name
                student[3],  # last_name
                student[4],  # email
                student[5],  # phone
                student[7],  # city (index 7, not 6)
                active_status,
                str(student[12])  # joining_date
            ))

        print("└" + "─" * 150 + "┘")

    except Exception as e:
        print(f"❌ Error retrieving data: {e}")
    finally:
        cursor.close()
        conn.close()

def retrieve_specific_student(enrollment_number):
    """Retrieve a specific student by enrollment number"""
    conn = connect_mysql()
    if not conn:
        return

    try:
        cursor = conn.cursor()

        # Get specific student
        query = "SELECT * FROM testapp_student WHERE enrollment_number = %s"
        cursor.execute(query, (enrollment_number,))
        student = cursor.fetchone()

        if student:
            print(f"\n=== STUDENT DETAILS FOR: {enrollment_number} ===\n")
            print(f"ID: {student[0]}")
            print(f"Enrollment Number: {student[1]}")
            print(f"Full Name: {student[2]} {student[3]}")
            print(f"Email: {student[4]}")
            print(f"Phone: {student[5]}")
            print(f"Date of Birth: {student[6] if student[6] else 'Not provided'}")
            print(f"Gender: {student[7] if student[7] else 'Not specified'}")
            print(f"Address: {student[8] if student[8] else 'Not provided'}")
            print(f"City: {student[9] if student[9] else 'Not provided'}")
            print(f"State: {student[10] if student[10] else 'Not provided'}")
            print(f"Zipcode: {student[11] if student[11] else 'Not provided'}")
            print(f"Joining Date: {student[12]}")
            print(f"Is Active: {'Yes' if student[13] else 'No'}")
            print(f"Created At: {student[14]}")
            print(f"Updated At: {student[15]}")
        else:
            print(f"❌ No student found with enrollment number: {enrollment_number}")

    except Exception as e:
        print(f"❌ Error retrieving student: {e}")
    finally:
        cursor.close()
        conn.close()

def get_table_info():
    """Get table structure information"""
    conn = connect_mysql()
    if not conn:
        return

    try:
        cursor = conn.cursor()

        # Get table structure
        cursor.execute("DESCRIBE testapp_student")
        columns = cursor.fetchall()

        print("\n=== TABLE STRUCTURE: testapp_student ===\n")
        print("┌" + "─" * 80 + "┐")
        print("│ {:<20} │ {:<15} │ {:<8} │ {:<5} │ {:<10} │ {:<10} │".format(
            "Column Name", "Type", "Null", "Key", "Default", "Extra"
        ))
        print("├" + "─" * 80 + "┤")

        for col in columns:
            print("│ {:<20} │ {:<15} │ {:<8} │ {:<5} │ {:<10} │ {:<10} │".format(
                col[0], col[1], col[2], col[3] or "", str(col[4])[:10] if col[4] else "", col[5]
            ))

        print("└" + "─" * 80 + "┘")

        # Get row count
        cursor.execute("SELECT COUNT(*) FROM testapp_student")
        count = cursor.fetchone()[0]
        print(f"\nTotal rows in table: {count}")

    except Exception as e:
        print(f"❌ Error getting table info: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    print("🔍 Retrieving data from MySQL database: student_management_system")
    print("📋 Table: testapp_student\n")

    # Show table structure
    get_table_info()

    # Show all students
    retrieve_all_students()

    # Show specific student
    retrieve_specific_student("20J21A0565")

    print("\n" + "="*60)
    print("✅ Data retrieval completed successfully!")
    print("="*60)