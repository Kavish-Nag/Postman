# Postman
Python-Postman 
Here's a README file for your Flask application:

---

# Flask Application

This is a simple Flask application that demonstrates basic routing and HTTP methods. The application has several endpoints that return text based on the provided routes and parameters. The app also allows you to update a stored age value using a POST request.

## Prerequisites

To run this application, you'll need:

- Python installed (version 3.x recommended)
- Flask installed (`pip install flask`)

## Running the Application

1. **Clone the repository** or create a file with the provided Flask code.
2. **Install Flask** if you haven't already:
   ```bash
   pip install flask
   ```
3. **Run the application**:
   ```bash
   python <your_filename>.py
   ```
   Replace `<your_filename>` with the name of the file containing the Flask code.

4. The application will start on `http://127.0.0.1:5000/`.

## Endpoints

### 1. `GET /`

- **Description**: Returns a simple greeting.
- **Example**:
  ```
  curl http://127.0.0.1:5000/
  ```
- **Response**: 
  ```
  Hello world!
  ```

### 2. `GET /sheela`

- **Description**: Returns a message including the stored age.
- **Example**:
  ```
  curl http://127.0.0.1:5000/sheela
  ```
- **Response**: 
  ```
  Sheela ki jawan 26!
  ```

### 3. `GET /sheela/<age>`

- **Description**: Takes an age as a URL parameter and returns a message with that age.
- **Example**:
  ```
  curl http://127.0.0.1:5000/sheela/30
  ```
- **Response**: 
  ```
  Sheela ki age 30.
  ```

### 4. `POST /sheela`

- **Description**: Updates the stored age value using a form parameter and returns a confirmation.
- **Example** (using Postman or `curl`):
  ```bash
  curl -X POST -F "age=30" http://127.0.0.1:5000/sheela
  ```
- **Response**: 
  ```
  DONE
  ```

  **Note**: The function currently does not properly update the `stored_age` due to incorrect placement of the `global` keyword and logic in the function.


## Testing with Postman

1. **GET Requests**: 
   - Open Postman and create a new GET request to `http://127.0.0.1:5000/` to test the root endpoint.
   - Create another GET request to `http://127.0.0.1:5000/sheela` to see the stored age.
   - Test dynamic age using `http://127.0.0.1:5000/sheela/30`.

2. **POST Requests**:
   - Open Postman and create a new POST request to `http://127.0.0.1:5000/sheela`.
   - Under the "Body" tab, select "form-data" and add a key-value pair with `key = age` and `value = <your_desired_age>`.
   - Click "Send" to see the response.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify the README to better suit your needs or to add more information about your application!
