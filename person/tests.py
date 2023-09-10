import requests

# Base URL for the API
base_url = 'http://127.0.0.1:8000/api'

# Function to print response content and status
def print_response(response):
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.content)

# CREATE (POST)
create_data = {'name': 'Mark Essien'}
response = requests.post(base_url, data=create_data)
print("CREATE (POST) Operation:")
print_response(response)

# READ (GET) - Fetch details of a person by name
read_params = {'name': 'Mark Essien'}
response = requests.get(base_url, params=read_params)
print("\nREAD (GET) Operation (Fetch details of a person by name):")
print_response(response)

# Get the person's ID from the previous response
person_id = response.json()['id']

# UPDATE (PUT) - Modify the details of an existing person
update_data = {'id': person_id, 'name': 'Essien Mark'}
response = requests.put(base_url, data=update_data)
print("\nUPDATE (PUT) Operation (Modify the details of an existing person):")
print_response(response)

# DELETE - Remove a person by ID
delete_data = {'id': person_id}
response = requests.delete(base_url, data=delete_data)
print("\nDELETE Operation (Remove a person by ID):")
print_response(response)
