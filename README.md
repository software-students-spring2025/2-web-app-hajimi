# Web Application Exercise

A little exercise to build a web application following an agile development process. See the [instructions](instructions.md) for more detail.

## Product vision statement

Our Inventory Management System is designed to streamline and optimize product management for stores and warehouses. By providing an intuitive and efficient platform, users can seamlessly add, edit, delete, and search for products, while maintaining a clear overview of stock levels.
This system aims to reduce inventory errors, enhance operational efficiency, and improve decision-making through real-time data accessibility. With a user-friendly interface and a robust backend powered by Flask and MongoDB, our solution ensures reliability and scalability for businesses of all sizes. Our vision is to create a seamless, accurate, and efficient inventory management experience, empowering businesses to focus on growth while minimizing stock-related inefficiencies.

## User stories

See instructions. Delete this line and place a link to the user stories here.

## Steps necessary to run the software

# Flask + MongoDB Web Application

## Product Vision Statement
A simple inventory management web application that allows users to add, edit, delete, and search for products using a MongoDB backend and Flask framework.

## Prerequisites
Ensure you have the following installed on your system:

- **Python 3.8+**
- **MongoDB** (Local or Remote)
- **pip** (Python package manager)
- **Git**
- **Virtual Environment (venv) (Optional but recommended)**

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/your-project.git
cd your-project
```

### 2. Set Up a Virtual Environment (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project's root directory and define the following variables:

```ini
FLASK_APP=app.py
FLASK_ENV=development
MONGO_URI=mongodb://localhost:27017/your_database
SECRET_KEY=your_secret_key
```
- If using **MongoDB Atlas**, replace `MONGO_URI` with your Atlas connection string.
- Do **not** commit the `.env` file to version control.
- Share the `.env` file securely via the team’s messenger system.

### 5. Create an `env.example` File
Create a file named `env.example` in the repository to show the expected environment variable format without actual credentials:

```ini
FLASK_APP=app.py
FLASK_ENV=development
MONGO_URI=mongodb://localhost:27017/example_db
SECRET_KEY=your_secret_key_here
```

### 6. Start MongoDB (If Running Locally)
Ensure MongoDB is running before starting the Flask application:

#### On macOS/Linux:
```sh
mongod --dbpath /path/to/mongodb/data
```

#### On Windows:
```sh
net start MongoDB  # If installed as a service
```

### 7. Run the Application
```sh
flask run
```
By default, the app runs on **http://127.0.0.1:5000**.

### 8. Access the Application (Example Screens)
- **Home Page (`/`)** - Displays all products (data retrieved from the database).
- **Add Product (`/add`)** - Allows adding a new product.
- **Edit Product (`/edit/<product_id>`)** - Allows modifying an existing product.
- **Delete Product (`/delete/<product_id>`)** - Deletes a product.
- **Search Product (`/search`)** - Enables product search functionality.
- **Product Detail (`/item/<product_id>`)** - Displays details of a single product.

## User Authentication (Optional)
If authentication is required, install and configure **Flask-Login**:
```sh
pip install flask-login
```
Follow Flask-Login documentation for integrating authentication.

## Agile Development Practices
- **Discord Communication:** Use the team’s Discord channel (e.g., `#team-7`).
- **User Stories:** Documented as Issues on GitHub.
- **GitHub Issues Link:** [GitHub Issues](https://github.com/YOUR_GITHUB_USERNAME/your-project/issues)

## Deployment
For production, use **gunicorn** or **uWSGI** with **nginx**. Example:
```sh
gunicorn -w 4 app:app
```

## License
This project is licensed under the **MIT License**.



## Task boards

See instructions. Delete this line and place a link to the task boards here.
