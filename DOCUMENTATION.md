# Person API Documentation

Welcome to the Person API documentation. This document provides information about the API's endpoints, request and response formats, sample usage, known limitations, and setup instructions.

## Endpoints

### Create (POST)

**Request Format:**

- Method: POST
- Endpoint: `https://stagetwo.onrender.com/api`
- Request Body: JSON data with the `"name"` field.

**Response Format:**

- Status Code: 201 Created (on successful creation)
- JSON Response: The created person object.

### Read (GET)

**Retrieve by ID:**

- Method: GET
- Endpoint: `https://stagetwo.onrender.com/api/<user_id>`
- Response Format: JSON containing person details.

### Update (PUT)

**Request Format:**

- Method: PUT
- Endpoint: `https://stagetwo.onrender.com/api`
- Request Body: JSON data with the `"id"` (person ID) and `"name"` fields.

**Response Format:**

- JSON Response: The updated person object.

### Delete (DELETE)

**Delete by Name:**

- Method: DELETE
- Endpoint: `https://stagetwo.onrender.com/api`
- Request Body: JSON data with the `"name"` field.

**Delete by ID:**

- Method: DELETE
- Endpoint: `https://stagetwo.onrender.com/api`
- Request Body: JSON data with the `"id"` field.

**Response Format:**

- Status Code: 204 No Content (on successful deletion)

## Sample Usage

### Create (POST)

**Example Request:**

```bash
curl -X POST -d '{"name": "John Doe"}' -H 'Content-Type: application/json' https://stagetwo.onrender.com/api
```

**Expected Response (JSON):**

```json
{
  "id": 1,
  "name": "John Doe"
}
```

### Read (GET)

**Retrieve by ID:**

**Example Request:**

```bash
curl https://stagetwo.onrender.com/api/1
```

**Expected Response (JSON):**

```json
{
  "id": 1,
  "name": "John Doe"
}
```

### Update (PUT)

**Example Request:**

```bash
curl -X PUT -d '{"id": 1, "name": "Updated Name"}' -H 'Content-Type: application/json' https://stagetwo.onrender.com/api
```

**Expected Response (JSON):**

```json
{
  "id": 1,
  "name": "Updated Name"
}
```

### Delete (DELETE)

**Delete by Name:**

**Example Request:**

```bash
curl -X DELETE -d '{"name": "John Doe"}' -H 'Content-Type: application/json' https://stagetwo.onrender.com/api
```

**Expected Response (No Content):**

```text
HTTP/1.1 204 No Content
```

**Delete by ID:**

**Example Request:**

```bash
curl -X DELETE -d '{"id": 1}' -H 'Content-Type: application/json' https://stagetwo.onrender.com/api
```

**Expected Response (No Content):**

```text
HTTP/1.1 204 No Content
```

## Known Limitations and Assumptions

- The API does not support multiple people with the same name.
- The API does not implement authentication or authorization.

## Local Setup and Deployment

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/Shullyd7/HNGX_stage_two
   ```

2. Navigate to the project directory.

   ```bash
   cd HNGX_stage_two
   ```

3. Create a virtual environment and activate it.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install project dependencies.

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations.

   ```bash
   python manage.py migrate
   ```

6. Start the development server.

   ```bash
   python manage.py runserver
   ```

7. The API will be accessible at `http://127.0.0.1:8000/api`.

## Running Tests

Automated tests for the API are available in `person/tests.py`. To run the tests, navigate to the `person` folder and execute the following command:

```bash
python tests.py
```