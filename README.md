### Project Title: Flask Blog with One-to-Many Relationship

---

### Flask Blog with One-to-Many Relationship

This project demonstrates a simple blog application built using Flask, SQLAlchemy, and WTForms, focusing on managing a one-to-many relationship between blog posts and comments.

#### Features:

- **User Management**: Create, update, and delete user accounts.
- **Blog Posts**: Allow users to create, update, and delete their blog posts.
- **Comments**: Enable users to leave comments on blog posts.
- **CRUD Operations**: Implement full CRUD functionality for users, posts, and comments.

#### Technologies Used:

- **Flask**: Micro-framework for web development in Python.
- **Flask-SQLAlchemy**: Flask extension for easy integration with SQLAlchemy.
- **WTForms**: Library for form validation and rendering.
- **Jinja2**: Templating engine for Flask.
- **SQLite/PostgreSQL/MySQL**: Choose a database backend for data storage.

#### Getting Started:

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/flask-blog.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

4. Run the application:

   ```bash
   flask run
   ```

5. Access the application in your web browser at `http://localhost:5000`.

#### Contributing:

Contributions are welcome! Please follow the guidelines outlined in CONTRIBUTING.md.

#### License:

This project is licensed under the MIT License. See the LICENSE file for details.
