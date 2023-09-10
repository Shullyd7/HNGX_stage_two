# Person API

The **Person API** is a simple Django application that allows you to manage a list of people. You can perform CRUD (Create, Read, Update, Delete) operations on person records.

## Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Shullyd7/HNGX_stage_two
   ```

2. Navigate to the project directory:

   ```bash
   cd HNGX_stage_two
   ```

3. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. The API will be accessible at `http://127.0.0.1:8000/api`.


## Deployment

The API has been deployed and can be accessed at [https://stagetwo.onrender.com/api](https://stagetwo.onrender.com/api).


## API Endpoints

### Create (POST)

To create a new person record, send a POST request to the following endpoint:

- Endpoint: `https://stagetwo.onrender.com/api`
- Request Body: JSON data with the `"name"` field.

Example:

```bash
curl -X POST -d '{"name": "John Doe"}' -H 'Content-Type: application/json' https://stagetwo.onrender.com/api
```

### Read (GET)

To retrieve details of a person, you can use either their name or ID. Send a GET request to one of the following endpoints:

- Retrieve by Name:
  - Endpoint: `https://stagetwo.onrender.com/api?name=John Doe`

- Retrieve by ID (replace `1` with the actual person ID):
  - Endpoint: `https://stagetwo.onrender.com/api?id=1`

Example:

```bash
# Retrieve by Name
curl https://stagetwo.onrender.com/api?name=John Doe

# Retrieve by ID
curl https://stagetwo.onrender.com/api?id=1
```

### Update (PUT)

To update the details of an existing person, send a PUT request to the following endpoint:

- Endpoint: `https://stagetwo.onrender.com/api`
- Request Body: JSON data with the `"id"` (person ID) and `"name"` fields.

Example:

```bash
curl -X PUT -d '{"id": 1, "name": "Updated Name"}' -H 'Content-Type: application/json' https://stagetwo.onrender.com/api
```

### Delete (DELETE)

To delete a person record, send a DELETE request to one of the following endpoints:

- Delete by Name:
  - Endpoint: `https://stagetwo.onrender.com/api`
  - Request Body: JSON data with the `"name"` field.

- Delete by ID (replace `1` with the actual person ID):
  - Endpoint: `https://stagetwo.onrender.com/api`
  - Request Body: JSON data with the `"id"` field.

Example:

```bash
# Delete by Name
curl -X DELETE -d '{"name": "John Doe"}' -H 'Content-Type: application/json' https://stagetwo.onrender.com/api

# Delete by ID
curl -X DELETE -d '{"id": 1}' -H 'Content-Type: application/json' https://stagetwo.onrender.com/api
```