import socket
import qrcode
import os

def generate_access_info():
    """Generate access information for Android users"""

    # Get network IP
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    access_info = f"""
STUDENT MANAGEMENT SYSTEM - ANDROID ACCESS
{'='*50}

FIXED: Site is now reachable from Android devices!

WRONG URL (Only works on this computer):
   http://127.0.0.1:8000/

CORRECT URL (Works on Android devices):
   http://192.168.1.6:8000/

HOW TO ACCESS FROM ANDROID:

1. Connect your Android device to the SAME WiFi network
2. Open Chrome/Safari browser
3. Go to: http://192.168.1.6:8000/
4. Start using the Student Management System!

AVAILABLE FEATURES:
   • Dashboard - View student statistics
   • Student List - Browse all students
   • Add Student - Create new records
   • Edit Student - Update information
   • Delete Student - Remove records
   • Search - Find students quickly

API ENDPOINTS (For Android Apps):
   • GET  /api/students/         - List all students
   • GET  /api/students/<id>/    - Get student details
   • POST /api/students/         - Create new student
   • PUT  /api/students/<id>/    - Update student
   • DELETE /api/students/<id>/  - Delete student

ADMIN ACCESS:
   URL: http://192.168.1.6:8000/admin/
   Username: admin
   Password: admin

IMPORTANT NOTES:
   • Both devices must be on the same WiFi network
   • Server must be running: python manage.py runserver 0.0.0.0:8000
   • Firewall should allow port 8000
   • ALLOWED_HOSTS configured for network access
   • For external access, consider ngrok or similar tools

QUICK START:
   1. Share this URL: http://192.168.1.6:8000/
   2. Android users connect to same WiFi
   3. Open URL in mobile browser
   4. Enjoy full CRUD operations!

{'='*50}
"""

    # Save to file
    with open('android_access_guide.txt', 'w') as f:
        f.write(access_info)

    print("✅ Android access guide saved to: android_access_guide.txt")
    print("\n" + access_info)

    return local_ip

if __name__ == "__main__":
    ip = generate_access_info()
    print(f"\nShare this URL with Android users: http://{ip}:8000/")