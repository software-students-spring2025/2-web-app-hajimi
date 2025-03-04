# Web Application Exercise

A little exercise to build a web application following an agile development process. See the [instructions](instructions.md) for more detail.

## Product vision statement

Our Inventory Management System is designed to streamline and optimize product management for stores and warehouses. By providing an intuitive and efficient platform, users can seamlessly add, edit, delete, and search for products, while maintaining a clear overview of stock levels.
This system aims to reduce inventory errors, enhance operational efficiency, and improve decision-making through real-time data accessibility. With a user-friendly interface and a robust backend powered by Flask and MongoDB, our solution ensures reliability and scalability for businesses of all sizes. Our vision is to create a seamless, accurate, and efficient inventory management experience, empowering businesses to focus on growth while minimizing stock-related inefficiencies.

## User stories

- a user, I want to view detailed information about a product so that I can compare options, understand the price and availability, and make an informed purchasing decision.
- As an admin, I want to add new products to the system so that customers have access to the latest offerings and inventory remains up to date.
- As a user, I want to view a list of products on the home screen so that I can easily browse available items and quickly find what interests me. 
- As an admin, I want to edit existing product details so that any incorrect or outdated information can be updated to maintain accuracy and improve user trust.
- As an admin, I want to delete products from the database so that unavailable or discontinued items are removed, preventing confusion and maintaining a clean catalog.
- As a user, I want to search for products using keywords so that I can quickly find specific items without having to scroll through long lists.


## Steps necessary to run the software

## Prerequisites
Ensure you have the following installed on your system:

- **Python 3.8+**
- **MongoDB** (Local or Remote)
- **pip** (Python package manager)
- **Git**
- **Virtual Environment (venv) **

### 1. Clone the Repository
```sh
git clone https://github.com/software-students-spring2025/2-web-app-hajimi.git
cd 2-web-app-hajimi
```

### 2. Set Up a Virtual Environment 
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

### 5. Start MongoDB (If Running Locally)
Ensure MongoDB is running before starting the Flask application:

### 6. Run the Application
```sh
flask run
```
By default, the app runs on **http://127.0.0.1:5000**.


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
🔆 [Team Hajimi- Sprint 1](https://github.com/orgs/software-students-spring2025/projects/88/views/2)
🔆 [Team Hajimi- Sprint 2](https://github.com/orgs/software-students-spring2025/projects/136)
