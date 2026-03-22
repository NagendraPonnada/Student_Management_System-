import socket
import requests
import time

def test_connectivity():
    """Test network connectivity for Android access"""

    print("🔍 TESTING NETWORK CONNECTIVITY FOR ANDROID ACCESS")
    print("=" * 60)

    # Get network IP
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"📡 Your computer's network IP: {local_ip}")

    # Test local access
    try:
        response = requests.get(f"http://127.0.0.1:8000/", timeout=5)
        print(f"✅ Local access (127.0.0.1:8000): HTTP {response.status_code}")
    except Exception as e:
        print(f"❌ Local access failed: {e}")

    # Test network access
    try:
        response = requests.get(f"http://{local_ip}:8000/", timeout=5)
        print(f"✅ Network access ({local_ip}:8000): HTTP {response.status_code}")
    except Exception as e:
        print(f"❌ Network access failed: {e}")

    print("\n📱 TROUBLESHOOTING STEPS FOR ANDROID:")
    print("1. Ensure Android device is on the SAME WiFi network")
    print("2. Check if firewall is blocking port 8000")
    print("3. Try disabling Windows Firewall temporarily")
    print("4. Verify server is running: python manage.py runserver 0.0.0.0:8000")
    print("5. Test from another device on the same network")

    print(f"\n🔗 Share this URL with Android users: http://{local_ip}:8000/")

if __name__ == "__main__":
    test_connectivity()