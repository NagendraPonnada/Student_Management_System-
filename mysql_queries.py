import pymysql

def run_mysql_query(query, description):
    """Execute a MySQL query and display results"""
    print(f"\n=== {description} ===")

    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='student_management_system'
        )

        cursor = conn.cursor()

        # Execute the query
        cursor.execute(query)
        results = cursor.fetchall()

        if cursor.description:  # If it's a SELECT query
            columns = [desc[0] for desc in cursor.description]

            if not results:
                print("No data found.")
            else:
                # Print column headers
                print(" | ".join(f"{col:<15}" for col in columns))
                print("-" * (len(columns) * 18))

                # Print data rows
                for row in results:
                    print(" | ".join(f"{str(cell):<15}" for cell in row))
        else:
            print(f"Query executed successfully. Affected rows: {cursor.rowcount}")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"❌ Error: {e}")

# Different MySQL queries to retrieve data
queries = [
    ("SELECT * FROM testapp_student", "ALL STUDENT DATA"),
    ("SELECT enrollment_number, first_name, last_name, email, phone FROM testapp_student", "BASIC STUDENT INFO"),
    ("SELECT COUNT(*) as total_students FROM testapp_student", "TOTAL STUDENT COUNT"),
    ("SELECT * FROM testapp_student WHERE is_active = 1", "ACTIVE STUDENTS ONLY"),
    ("SELECT enrollment_number, first_name, last_name, city FROM testapp_student WHERE city LIKE '%Hyderabad%'", "STUDENTS FROM HYDERABAD"),
    ("SELECT enrollment_number, first_name, last_name, joining_date FROM testapp_student ORDER BY joining_date DESC", "STUDENTS BY JOINING DATE"),
    ("SELECT gender, COUNT(*) as count FROM testapp_student GROUP BY gender", "STUDENTS BY GENDER"),
]

if __name__ == "__main__":
    print("🔍 MySQL Data Retrieval Examples for testapp_student table")
    print("="*70)

    for query, description in queries:
        run_mysql_query(query, description)

    print("\n" + "="*70)
    print("✅ All queries completed successfully!")
    print("💡 Tip: You can run these queries directly in MySQL command line:")
    print("   mysql -u root -p student_management_system")
    print("="*70)