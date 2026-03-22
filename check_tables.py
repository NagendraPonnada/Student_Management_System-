import pymysql

# Connect to MySQL database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='student_management_system'
)

cursor = conn.cursor()

# Get all table names
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

print("Tables in student_management_system database:")
for table in tables:
    print(f"- {table[0]}")

# Get structure of the student table
print("\n\nStudent table structure:")
cursor.execute("DESCRIBE testapp_student")
columns = cursor.fetchall()

print("Column Name | Type | Null | Key | Default | Extra")
print("-" * 50)
for col in columns:
    print(f"{col[0]} | {col[1]} | {col[2]} | {col[3]} | {col[4]} | {col[5]}")

conn.close()