# 🚀 TaskFlow - Django Task Management App

TaskFlow is a modern task management web application built with Django that helps users organize and manage their daily tasks efficiently. It includes authentication, task management, searching, filtering, sorting, pagination, and a clean user interface.

---

## 🌐 Live Demo

https://taskflow-vh1v.onrender.com

---

## ✨ Features

- User Authentication (Register, Login, Logout)
- Create, Update and Delete Tasks
- Mark Tasks as Completed or Pending
- Search Tasks
- Filter Tasks
- Sort Tasks
- Task Categories
- Task Priority Levels
- Due Date Tracking
- Task Status (Upcoming, Due Today, Overdue)
- Dashboard Statistics
- Progress Bar
- Pagination
- User-specific Task Management

---

## 🛠️ Technologies Used

- Python
- Django
- HTML5
- CSS3
- SQLite
- Gunicorn
- WhiteNoise
- Render

---

## 🚀 Installation

```bash
git clone https://github.com/BIwashbhatarai/TaskFlow.git

cd TaskFlow

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## 🚀 Deployment

- Hosted on Render
- Gunicorn used as the WSGI server
- WhiteNoise used to serve static files
- Production configuration with `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS`

---

## 📌 Future Improvements

- Dark Mode
- Email Notifications
- File Attachments
- REST API
- Docker Support

---

## 👨‍💻 Author

**Tilak Bhattarai**
