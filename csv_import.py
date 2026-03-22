import csv
import pymysql
import os

def create_sample_csv():
    """Create a sample CSV file for student data"""
    sample_data = [
        ['enrollment_number', 'first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'gender', 'address', 'city', 'state', 'zipcode'],
        ['22J21A0001', 'Alice', 'Johnson', 'alice.johnson@example.com', '9876543212', '2002-03-10', 'F', '789 Pine St', 'Bangalore', 'Karnataka', '560001'],
        ['22J21A0002', 'Bob', 'Wilson', 'bob.wilson@example.com', '9876543213', '2001-11-25', 'M', '321 Elm St', 'Chennai', 'Tamil Nadu', '600001'],
        ['22J21A0003', 'Carol', 'Brown', 'carol.brown@example.com', '9876543214', '2002-07-08', 'F', '654 Maple Ave', 'Pune', 'Maharashtra', '411001'],
        ['22J21A0004', 'David', 'Davis', 'david.davis@example.com', '9876543215', '2001-12-30', 'M', '987 Cedar Ln', 'Kolkata', 'West Bengal', '700001']
    ]

    with open('sample_students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(sample_data)

    print("✅ Sample CSV file 'sample_students.csv' created!")

def import_csv_to_mysql(csv_file):
    """Import student data from CSV file to MySQL"""
    if not os.path.exists(csv_file):
        print(f"❌ File '{csv_file}' not found!")
        return

    try:
        # Connect to database
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='student_management_system'
        )

        cursor = conn.cursor()

        # Read CSV file
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Skip header row

            added_count = 0
            for row in csv_reader:
                try:
                    # Insert query
                    query = """
                    INSERT INTO testapp_student
                    (enrollment_number, first_name, last_name, email, phone, date_of_birth,
                     gender, address, city, state, zipcode, joining_date, is_active, created_at, updated_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURDATE(), 1, NOW(), NOW())
                    """

                    # Handle empty date_of_birth
                    dob = row[5] if row[5] else None
                    gender = row[6] if row[6] else None

                    values = (
                        row[0], row[1], row[2], row[3], row[4], dob,
                        gender, row[7], row[8], row[9], row[10]
                    )

                    cursor.execute(query, values)
                    added_count += 1
                    print(f"✅ Added: {row[1]} {row[2]} ({row[0]})")

                except pymysql.Error as e:
                    print(f"❌ Failed to add {row[1]} {row[2]}: {e}")

        conn.commit()
        print(f"\n✅ Successfully imported {added_count} students from CSV!")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if 'conn' in locals():
            cursor.close()
            conn.close()

def show_csv_format():
    """Show the required CSV format"""
    print("=== CSV FILE FORMAT ===")
    print("Create a CSV file with the following columns (header row required):")
    print("")
    print("enrollment_number,first_name,last_name,email,phone,date_of_birth,gender,address,city,state,zipcode")
    print("")
    print("Example data:")
    print("22J21A0001,Alice,Johnson,alice@example.com,9876543210,2002-03-10,F,123 Main St,Mumbai,Maharashtra,400001")
    print("22J21A0002,Bob,Smith,bob@example.com,9876543211,2001-05-15,M,456 Oak Ave,Delhi,Delhi,110001")
    print("")
    print("Notes:")
    print("- date_of_birth: Use YYYY-MM-DD format or leave empty")
    print("- gender: M (Male), F (Female), O (Other), or leave empty")
    print("- All other fields are required")

if __name__ == "__main__":
    print("📊 STUDENT DATA IMPORT FROM CSV")
    print("=" * 40)

    while True:
        print("\nChoose an option:")
        print("1. Create sample CSV file")
        print("2. Import from CSV file")
        print("3. Show CSV format requirements")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == '1':
            create_sample_csv()
        elif choice == '2':
            csv_file = input("Enter CSV filename (e.g., students.csv): ").strip()
            import_csv_to_mysql(csv_file)
        elif choice == '3':
            show_csv_format()
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

        input("\nPress Enter to continue...")