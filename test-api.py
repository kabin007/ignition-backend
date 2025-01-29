import requests

# Base URL
base_url = "http://localhost:8000/api/users/student/"

# Student ID to update
student_id = 16  # Replace with the actual student ID

# Data to update in the required format
data = {
    "basic_info": {
        "first_name": "Avi",
        "last_name": "Bickle",
        "dob": "1940-01-01",
        "gender": "Male",
        "marital_status": "Single",
        "passport_no": "123456789",
    },
    "contact": {
        "email": "travis.bickle@example.com",
        "phone": "+1234567890",
        "alternate_phone": "+0987654321",
    },
    "address": {
        "street": "Mechinagar,11",
        "city": "Sanischare",
        "state": "Koshi",
        "postal_code": "57207",
        "country": "2",
    },
}

# Send PUT request
try:
    response = requests.put(
        url=f"{base_url}{student_id}/",  # URL for the specific student
        json=data,  # Send data as JSON
        headers={"Content-Type": "application/json"}  # Set appropriate headers
    )
    
    # Handle response
    if response.status_code == 200:
        print("Update successful!")
        print("Response:", response.json())
    else:
        print(f"Failed to update. Status code: {response.status_code}")
        print("Error:", response.text)

except requests.RequestException as e:
    print("An error occurred:", str(e))


'''
SERVER RESPONSE
Update successful!
Response: {'uuid': 15,
	   'basic_info': {'id': 4,
			 'first_name': 'Travis',
			 'last_name': 'Bickle',
			 'password': 'pbkdf2_sha256$870000$vd1FywlTpCoeWvDOvmZZ1Z$47kwaZL93nGSZhn018qcy3TgO9wHdMrHlqeX2Nfl6Ik=',
			 'dob': '1940-01-01',
			 'gender': 'Male',
			 'marital_status': 'Single',
			 'passport_no': '123456789'},
	   'contact': {'id': 4,
		       'email': 'travis.bickle@example.com',
		       'phone': '+1234567890', 
			'alternate_phone': '+0987654321'},
	   'address': {'id': 3,
			 'street': 'Mechinagar,11',
			 'city': 'Dhulabari', 
			'state': 'Koshi', 
			'postal_code': '57207', 
			'country': 1},
	 'profile_picture': None, 'created_at': '2025-01-14T16:42:46.732409Z', 'updated_at': '2025-01-14T17:04:45.280075Z',
	 'educational_background': None,
	 'study_preferences': None,
	 'documents': None}
'''
