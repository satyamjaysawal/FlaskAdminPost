
---
## Render Link : 
[https://flaskadminpost.onrender.com](https://flaskadminpost.onrender.com)


### 1. **Set Up the Environment**
   - Ensure you have Python installed on your machine.
   - Optionally, install `pip` if it's not already available.

### 2. **Create and Activate Virtual Environment**
   - Open a terminal and navigate to your project directory.
   - Run the following command to create a virtual environment:
     ```bash
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     - On **Windows**:
       ```bash
       venv\Scripts\activate
       ```
     - On **macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```

### 3. **Install Dependencies**
   - Install Flask and all required extensions by running:
     ```bash
     pip install Flask Flask-Login Flask-SQLAlchemy Flask-Migrate Flask-WTF Werkzeug
     ```

### 4. **Set Up the Project Structure**
   - Create the project folder structure as outlined:
     ```
     flask_app/
     │
     ├── app/
     │   ├── __init__.py
     │   ├── models.py
     │   ├── forms.py
     │   ├── routes.py
     │   ├── templates/
     │   │   └── (HTML templates like base.html, login.html, etc.)
     │   └── static/
     │       └── styles.css
     │
     ├── migrations/
     ├── config.py
     ├── requirements.txt
     ├── run.py
     └── README.md
     ```

### 5. **Write the Code**
   - Add the respective code files:
     - **`app/__init__.py`** to initialize Flask and its extensions.
     - **`app/models.py`** for database models (User, Post, Comment).
     - **`app/forms.py`** for Flask-WTF forms.
     - **`app/routes.py`** to define the routes for handling login, registration, posts, comments, etc.
     - **`run.py`** to run the app.
     - **HTML templates** in `app/templates/`.
   
### 6. **Set Up the Database**
   - To create the database, run the following commands:
     ```bash
     flask db init  # Initializes migration directory
     flask db migrate -m "Initial migration."  # Generates migration script
     flask db upgrade  # Applies the migration and creates the database
     ```

### 7. **Create the `requirements.txt` File**
   - Create the `requirements.txt` by running:
     ```bash
     pip freeze > requirements.txt
     ```

### 8. **Initialize Git Repository (Optional)**
   - If using version control, initialize a Git repository:
     ```bash
     git init
     ```

### 9. **Run the Flask Application**
   - Run the Flask app using:
     ```bash
     python run.py
     ```
   - The app will be accessible at `http://127.0.0.1:8000/`.

### 10. **Access the Application**
   - Open your browser and go to `http://127.0.0.1:8000/` to view the application.
   - You can log in, register users, add posts, and comment based on the routes and functionality provided.

### Deployed on Render (Each time take 50 sec for Server restart as there Free Policy):
- **Deploying**: When deploying, you may use `gunicorn` as the web server by running:
  ```bash
  gunicorn -w 4 run:app
  ```

[https://flaskadminpost.onrender.com](https://flaskadminpost.onrender.com)


![Screenshot 2024-10-13 131206](https://github.com/user-attachments/assets/35f4a51b-cd78-4811-83f1-9c1701290795)

![Screenshot 2024-10-13 131306](https://github.com/user-attachments/assets/226bd746-1de1-4330-9d18-6854a7a555e3)
![Screenshot 2024-10-13 131338](https://github.com/user-attachments/assets/d36bd753-99e2-427d-aafe-e0ab641525d6)
![Screenshot 2024-10-13 131429](https://github.com/user-attachments/assets/3c3619ef-73d1-4af7-aa93-a6fc3c7409c1)
![Screenshot 2024-10-13 131618](https://github.com/user-attachments/assets/853ea7dc-7301-4322-afb8-344ed834e4ba)
