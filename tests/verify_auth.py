import sys
import os
import json
import urllib.request
import urllib.error

# Add the project root to the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configuration
BASE_URL = "http://localhost:8000/api/v1"
TEST_USER = {
    "nome": "Test User",
    "email": "test_verification@example.com",
    "senha": "securepassword123",
    "cargo": "Tester",
    "permissao": "admin"
}

def highlight(text, color="green"):
    colors = {"green": "\033[92m", "red": "\033[91m", "reset": "\033[0m"}
    return f"{colors.get(color, '')}{text}{colors['reset']}"

def make_request(url, data=None):
    headers = {'Content-Type': 'application/json'}
    req = urllib.request.Request(url, headers=headers)
    
    if data:
        json_data = json.dumps(data).encode('utf-8')
        req.data = json_data
        
    try:
        with urllib.request.urlopen(req) as response:
            return response.status, json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()
    except Exception as e:
        return 0, str(e)

def run_verification():
    print("Starting Authentication Verification...")

    # 1. Create User
    print(f"\n1. Creating User: {TEST_USER['email']}")
    status, response_data = make_request(f"{BASE_URL}/usuarios/", TEST_USER)
    
    if status in [200, 201]:
        print(highlight("SUCCESS: User created successfully.", "green"))
        print(f"Response: {response_data}")
    elif status == 400 and "Email já cadastrado" in str(response_data):
         print(highlight("INFO: User already exists. Proceeding to login.", "green"))
    else:
        print(highlight(f"FAILURE: Could not create user. Status: {status}", "red"))
        print(response_data)
        return

    # 2. Login (Success Case)
    print(f"\n2. Testing Login (Correct Credentials)")
    login_data = {
        "email": TEST_USER["email"],
        "senha": TEST_USER["senha"]
    }
    status, response_data = make_request(f"{BASE_URL}/usuarios/login", login_data)
    
    if status == 200:
        if "access_token" in response_data:
             print(highlight("SUCCESS: Login successful. Token received.", "green"))
             print(f"Token Type: {response_data['token_type']}")
        else:
             print(highlight("FAILURE: No token in response.", "red"))
    else:
        print(highlight(f"FAILURE: Login failed. Status: {status}", "red"))
        print(response_data)

    # 3. Login (Failure Case)
    print(f"\n3. Testing Login (Wrong Password)")
    wrong_login_data = {
        "email": TEST_USER["email"],
        "senha": "wrongpassword"
    }
    status, response_data = make_request(f"{BASE_URL}/usuarios/login", wrong_login_data)

    if status == 401:
        print(highlight("SUCCESS: Login correctly rejected.", "green"))
    else:
        print(highlight(f"FAILURE: Expected 401, got {status}", "red"))

if __name__ == "__main__":
    run_verification()
