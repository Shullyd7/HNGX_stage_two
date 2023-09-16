# CRUD API

The **CRUD API** is a simple Django application that allows you to manage a list of people. You can perform CRUD (Create, Read, Update, Delete) operations on person records.

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

7. The API will be accessible at `http://127.0.0.1:8000/resources`.

## Deployment

The API has been deployed and can be accessed at [https://stagetwo.onrender.com/resources](https://stagetwo.onrender.com/resources).

## API Endpoints

### Create (POST)

To create a new person record, send a POST request to the following endpoint:

- Endpoint: `https://stagetwo.onrender.com/resources`
- Request Body: JSON data with the `"name"` field.

Example:

```bash
curl -X POST -d '{"name": "John Doe"}' -H 'Content-Type: application/json' https://stagetwo.onrender.com/resources
```

### Get All Users (GET)

To retrieve details of all persons. Send a GET request the following endpoint:

- Endpoint: `https://stagetwo.onrender.com/resources`

Example:

```bash
curl https://stagetwo.onrender.com/resources
```

### Read (GET)

To retrieve details of a person, you can use the ID. Send a GET request to the following endpoints:

- Retrieve by ID (replace `1` with the actual person ID):
  - Endpoint: `https://stagetwo.onrender.com/resources/1`

Example:

```bash
# Retrieve by ID
curl https://stagetwo.onrender.com/resources/1
```

### Update (PUT)

To update the details of an existing person, send a PUT request to the following endpoint:

- Retrieve by ID (replace `1` with the actual person ID):
  - Endpoint: `https://stagetwo.onrender.com/resources/1`
  - Request Body: JSON data with the`"name"` field.

Example:

```bash
curl -X PUT -d '{"name": "Updated Name"}' -H 'Content-Type: application/json' https://stagetwo.onrender.com/resources
```

### Delete (DELETE)

To delete a person record, send a DELETE request to the following endpoints:

- Delete by ID (replace `1` with the actual person ID):
  - Endpoint: `https://stagetwo.onrender.com/resources/1`

Example:

```bash
# Delete by ID
curl -X DELETE https://stagetwo.onrender.com/resources/1
```

```