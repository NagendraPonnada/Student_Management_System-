import pymysql

def get_student_data():
    """Retrieve actual student data from MySQL"""
    try:
        # Connect to MySQL
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='student_management_system'
        )

        cursor = conn.cursor()

        # Query to get all student data
        cursor.execute("SELECT * FROM testapp_student")

        # Fetch all rows
        students = cursor.fetchall()

        print("=== STUDENT DATA FROM testapp_student TABLE ===\n")

        if not students:
            print("❌ No data found in the table!")
            print("The table exists but contains no records.")
        else:
            print(f"✅ Found {len(students)} student(s) in the database:\n")

            # Display data in a readable format
            for i, student in enumerate(students, 1):
                print(f"--- Student {i} ---")
                print(f"ID: {student[0]}")
                print(f"Enrollment Number: {student[1]}")
                print(f"First Name: {student[2]}")
                print(f"Last Name: {student[3]}")
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
                print("-" * 50)

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"❌ Error: {e}")

def check_table_exists():
    """Check if table exists and get row count"""
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='student_management_system'
        )

        cursor = conn.cursor()

        # Check if table exists
        cursor.execute("SHOW TABLES LIKE 'testapp_student'")
        table_exists = cursor.fetchone()

        if table_exists:
            print("✅ Table 'testapp_student' exists in database")

            # Get row count
            cursor.execute("SELECT COUNT(*) FROM testapp_student")
            count = cursor.fetchone()[0]
            print(f"📊 Total rows in table: {count}")

            if count == 0:
                print("⚠️  Table is empty - no data to retrieve")
            else:
                print("✅ Table contains data - ready for retrieval")
        else:
            print("❌ Table 'testapp_student' does not exist")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    print("🔍 Checking MySQL Database Connection and Data...\n")

    # First check if table exists and has data
    check_table_exists()

    print("\n" + "="*60)

    # Then retrieve the actual data
    get_student_data()

    print("\n" + "="*60)
    print("📝 MySQL Commands to retrieve data manually:")
    print("mysql -u root -p")
    print("USE student_management_system;")
    print("SELECT * FROM testapp_student;")
    print("="*60)