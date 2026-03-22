import pymysql

def add_student_mysql():
    """Add a student directly to MySQL database"""
    print("=== ADD STUDENT VIA MYSQL ===\n")

    # Get user input
    enrollment = input("Enter Enrollment Number: ").strip()
    first_name = input("Enter First Name: ").strip()
    last_name = input("Enter Last Name: ").strip()
    email = input("Enter Email: ").strip()
    phone = input("Enter Phone: ").strip()
    dob = input("Enter Date of Birth (YYYY-MM-DD): ").strip() or None
    gender = input("Enter Gender (M/F/O): ").strip().upper() or None
    address = input("Enter Address: ").strip()
    city = input("Enter City: ").strip()
    state = input("Enter State: ").strip()
    zipcode = input("Enter Zipcode: ").strip()

    try:
        # Connect to database
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='student_management_system'
        )

        cursor = conn.cursor()

        # Insert query
        query = """
        INSERT INTO testapp_student
        (enrollment_number, first_name, last_name, email, phone, date_of_birth,
         gender, address, city, state, zipcode, joining_date, is_active, created_at, updated_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURDATE(), 1, NOW(), NOW())
        """

        values = (enrollment, first_name, last_name, email, phone, dob,
                 gender, address, city, state, zipcode)

        cursor.execute(query, values)
        conn.commit()

        print(f"✅ Student '{first_name} {last_name}' added successfully!")
        print(f"📋 Enrollment Number: {enrollment}")

    except pymysql.Error as e:
        print(f"❌ Database Error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if 'conn' in locals():
            cursor.close()
            conn.close()

def add_multiple_students():
    """Add multiple students in batch"""
    print("=== ADD MULTIPLE STUDENTS ===\n")

    students_data = [
        {
            'enrollment': '21J21A0001',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '9876543210',
            'dob': '2001-05-15',
            'gender': 'M',
            'address': '123 Main St',
            'city': 'Mumbai',
            'state': 'Maharashtra',
            'zipcode': '400001'
        },
        {
            'enrollment': '21J21A0002',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane.smith@example.com',
            'phone': '9876543211',
            'dob': '2001-08-20',
            'gender': 'F',
            'address': '456 Oak Ave',
            'city': 'Delhi',
            'state': 'Delhi',
            'zipcode': '110001'
        }
    ]

    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='student_management_system'
        )

        cursor = conn.cursor()

        added_count = 0
        for student in students_data:
            try:
                query = """
                INSERT INTO testapp_student
                (enrollment_number, first_name, last_name, email, phone, date_of_birth,
                 gender, address, city, state, zipcode, joining_date, is_active, created_at, updated_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURDATE(), 1, NOW(), NOW())
                """

                values = (
                    student['enrollment'], student['first_name'], student['last_name'],
                    student['email'], student['phone'], student['dob'], student['gender'],
                    student['address'], student['city'], student['state'], student['zipcode']
                )

                cursor.execute(query, values)
                added_count += 1
                print(f"✅ Added: {student['first_name']} {student['last_name']} ({student['enrollment']})")

            except pymysql.Error as e:
                print(f"❌ Failed to add {student['first_name']} {student['last_name']}: {e}")

        conn.commit()
        print(f"\n✅ Successfully added {added_count} students!")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if 'conn' in locals():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    print("🎓 STUDENT MANAGEMENT SYSTEM - DATA ENTRY")
    print("=" * 50)

    while True:
        print("\nChoose an option:")
        print("1. Add single student (interactive)")
        print("2. Add sample students (batch)")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == '1':
            add_student_mysql()
        elif choice == '2':
            add_multiple_students()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

        input("\nPress Enter to continue...")