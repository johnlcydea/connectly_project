# Connectly Project

**Connectly Project** is a Django-based web application designed for managing posts. It demonstrates **key concepts of web development**, including:
- REST APIs
- Secure data handling
- Integration with GitHub for version control

## Features

- User-friendly interface for creating, reading, and managing posts
- API endpoints for CRUD operations (compatible with tools like Postman)
- Secure project setup with `.gitignore` for sensitive file exclusion

## Technologies Used

| Category | Technology |
|----------|------------|
| Backend | Django (Python) |
| Database | SQLite (Development) |
| Frontend | HTML Templates |
| Version Control | Git and GitHub |

## Setup Instructions

### Create a Repository

1. Go to [GitHub](https://github.com/)
2. Click on the **New Repository** button
3. Enter a repository name (e.g., `connectly_project`)
4. Set the repository to **Private** or **Public**, as needed
5. Click **Create Repository**

### Clone the Repository

```bash
git clone https://github.com/<your-username>/connectly_project.git
cd connectly_project
```

### Create a Virtual Environment

```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
# On Linux/Mac:
source env/bin/activate
# On Windows:
env\Scripts\activate
```

### Install Dependencies

Create a `requirements.txt` file with the following dependencies:

```text
Django>=3.2
djangorestframework
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Start the Development Server

```bash
python manage.py runserver
```

Access the application at: http://127.0.0.1:8000/

### Adding .gitignore File

Create a `.gitignore` file in the root directory with the following content:

```text
# Virtual environment
env/

# Python cache files
__pycache__/

# Database files
db.sqlite3

# VS Code settings
.vscode/

# Log files
*.log

# System files
.DS_Store

# Python environment files
*.env
```

Stage and commit the `.gitignore` file:

```bash
git add .gitignore
git commit -m "Add .gitignore file"
git push origin main
```

## API Endpoints

### Create Post
- **URL**: `/posts/create/`
- **Method**: `POST`
- **Request Body**:
```json
{
    "title": "Test Post",
    "content": "This is a test post.",
    "author": 1
}
```

### List Posts
- **URL**: `/posts/`
- **Method**: `GET`

### Retrieve Post Details
- **URL**: `/posts/<post_id>/`
- **Method**: `GET`

## Folder Structure

```plaintext
connectly_project/
├── connectly_project/    # Main project folder
│   ├── settings.py       # Django settings
│   ├── urls.py          # Project URLs
│   ├── wsgi.py          # WSGI config
├── posts/               # Django app
│   ├── templates/posts/ # HTML templates
│   ├── migrations/      # Database migrations
│   ├── models.py        # Data models
│   ├── serializers.py   # DRF serializers
│   ├── views.py         # Views (business logic)
│   ├── urls.py          # App URLs
├── db.sqlite3           # SQLite database (excluded by .gitignore)
├── manage.py            # Django CLI manager
```

## Future Enhancements

- Add user authentication for secure access
- Deploy to a cloud platform like **Heroku** or **AWS**
- Implement additional features:
  - Post categories
  - Comments on posts
