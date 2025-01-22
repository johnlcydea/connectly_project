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
