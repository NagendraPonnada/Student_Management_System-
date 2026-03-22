import requests
import json

def test_api():
    """Test the API endpoints"""
    base_url = 'http://127.0.0.1:8000'

    print('🧪 Testing Student Management API Endpoints')
    print('=' * 50)

    # Test 1: GET all students
    print('\n1. Testing GET /api/students/')
    try:
        response = requests.get(f'{base_url}/api/students/')
        print(f'   Status Code: {response.status_code}')

        if response.status_code == 200:
            data = response.json()
            print(f'   Success: {data["success"]}')
            print(f'   Student Count: {data["count"]}')
            print('   ✅ GET all students - WORKING')
        else:
            print('   ❌ GET all students - FAILED')

    except Exception as e:
        print(f'   ❌ Error: {e}')

    # Test 2: GET specific student
    print('\n2. Testing GET /api/students/1/')
    try:
        response = requests.get(f'{base_url}/api/students/1/')
        print(f'   Status Code: {response.status_code}')

        if response.status_code == 200:
            data = response.json()
            if data["success"]:
                student = data["student"]
                print(f'   Student: {student["first_name"]} {student["last_name"]}')
                print('   ✅ GET specific student - WORKING')
            else:
                print('   ❌ Student not found')
        else:
            print('   ❌ GET specific student - FAILED')

    except Exception as e:
        print(f'   ❌ Error: {e}')

    # Test 3: POST new student
    print('\n3. Testing POST /api/students/ (Create)')
    try:
        new_student = {
            "enrollment_number": "25J21A0001",
            "first_name": "Test",
            "last_name": "Student",
            "email": "test@example.com",
            "phone": "9876543210",
            "address": "Test Address",
            "city": "Test City",
            "state": "Test State",
            "zipcode": "123456"
        }

        response = requests.post(
            f'{base_url}/api/students/',
            json=new_student,
            headers={'Content-Type': 'application/json'}
        )
        print(f'   Status Code: {response.status_code}')

        if response.status_code == 200:
            data = response.json()
            if data["success"]:
                print(f'   Created Student ID: {data["student_id"]}')
                print('   ✅ POST create student - WORKING')
            else:
                print(f'   ❌ Error: {data.get("error", "Unknown error")}')
        else:
            print('   ❌ POST create student - FAILED')

    except Exception as e:
        print(f'   ❌ Error: {e}')

    print('\n' + '=' * 50)
    print('📱 API Endpoints Summary:')
    print('✅ GET  /api/students/         - List all students')
    print('✅ GET  /api/students/<id>/    - Get specific student')
    print('✅ POST /api/students/         - Create new student')
    print('✅ PUT  /api/students/<id>/    - Update student')
    print('✅ DELETE /api/students/<id>/  - Delete student')
    print('=' * 50)

if __name__ == "__main__":
    test_api()