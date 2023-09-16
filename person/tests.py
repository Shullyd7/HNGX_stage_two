# Import the requests library at the beginning of your script
import requests

# Base URL for the API on your local development server
base_url = 'https://stagetwo.onrender.com/resources'

# Function to print response content and status
def print_response(response):
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.content)

# CREATE (POST)
create_data = {'name': 'Mark Essien'}
response = requests.post(base_url, data=create_data)
print("CREATE (POST) Operation:")
print_response(response)

# READ (GET) - Fetch details of a person by ID
person_id = response.json().get('id')
read_url = f'{base_url}/{person_id}'
response = requests.get(read_url)
print("\nREAD (GET) Operation (Fetch details of a person by ID):")
print_response(response)

# UPDATE (PUT) - Modify the details of an existing person
update_data = {'name': 'Essien Mark'}
response = requests.put(read_url, data=update_data)
print("\nUPDATE (PUT) Operation (Modify the details of an existing person):")
print_response(response)

# DELETE - Remove a person by ID
response = requests.delete(read_url)
print("\nDELETE Operation (Remove a person by ID):")
print_response(response)

# GET ALL USERS (GET)
all_users_url = f'{base_url}'  # URL for the "Get all users" API
response = requests.get(all_users_url)
print("\nGET ALL USERS Operation:")
print_response(response)
