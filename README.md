# User Profile Card Generator

A Flask-based web application that allows users to create personalized profile cards by submitting their information through a form. The application processes the submitted data, stores it in a SQLite database, and dynamically generates a professional profile card.

This project demonstrates full-stack web development fundamentals including form handling, POST requests, database integration, server-side validation, template rendering, and responsive frontend design.

---

## Features

- Create user profiles through a responsive form
- Live profile preview while entering details
- Real-time character counter for bio
- Live image preview using image URL
- Automatic fallback for invalid image URLs
- Server-side form validation
- Duplicate email validation
- Store profile information in SQLite database
- Dynamic profile card generation using Jinja2
- Flash messages for success and error notifications
- Responsive design for desktop and mobile devices
- Custom 404 error page

---

## Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Flask
- Jinja2

### Database

- SQLite
- SQLAlchemy ORM

---

## Project Structure

```text
User-Profile-Card-Generator/
│
├── database/
│   └── profile.db
│
├── models/
│   ├── __init__.py
│   └── profile.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── images/
│   │
│   └── js/
│       └── script.js
│
├── templates/
│   ├── index.html
│   └── profile.html
│
├── venv/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/User-Profile-Card-Generator.git
```

### 2. Navigate to the project directory

```bash
cd User-Profile-Card-Generator
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Application Workflow

1. Open the application.
2. Fill in the profile details.
3. Preview the profile in real time.
4. Submit the form.
5. The backend validates the input.
6. Profile information is stored in the SQLite database.
7. A dynamic profile card is generated and displayed.

---

## Form Fields

- Full Name
- Age
- Occupation
- Location
- Email Address
- Profile Image URL
- Bio

---

## Validation

The application performs both client-side and server-side validation.

- Required fields
- Email format validation
- Age range validation
- Bio character limit
- Duplicate email prevention
- Invalid image fallback

---

## Database Schema

| Column | Type |
|---------|------|
| id | Integer |
| name | String |
| age | Integer |
| occupation | String |
| location | String |
| email | String |
| image_url | String |
| bio | Text |
| created_at | DateTime |

---

## Skills Demonstrated

- Flask Application Development
- RESTful Routing
- POST Request Handling
- HTML Forms
- Jinja2 Template Rendering
- SQLite Database Integration
- SQLAlchemy ORM
- CRUD Fundamentals
- Server-side Validation
- JavaScript DOM Manipulation
- Responsive Web Design
- MVC Project Structure
- Error Handling

---

## Future Enhancements

- Profile editing
- Profile deletion
- User authentication
- Image upload support
- Search and filter profiles
- Dashboard with profile statistics
- Pagination
- Dark mode

---

## Requirements

- Python 3.10+
- Flask
- Flask-SQLAlchemy

Install all required packages using:

```bash
pip install -r requirements.txt
```

---

## Author

**Priyanshu Raj**

---

## License

This project is developed for educational and internship portfolio purposes.
<!-- Project review & docs log: 2026-10-27 [1/5] -->
<!-- Project review & docs log: 2026-10-29 [2/6] -->
