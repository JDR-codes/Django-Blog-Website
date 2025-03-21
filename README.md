# Blog Website

A fully functional blog website with user authentication, article management, likes, comments, and the ability to view articles only from followed users.

## Features
- **User Authentication**: Signup, login, and logout functionality.
- **User Profiles**: Users can follow and unfollow others.
- **Create & Manage Articles**: Users can write, edit, and delete their own articles.
- **Like & Comment**: Users can like and comment on articles.
- **Follow System**: Users can only view articles from people they follow.

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/blog-website.git
   cd blog-website
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```sh
   python manage.py migrate
   ```

5. **Create a Superuser (For Admin Access)**
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the Server**
   ```sh
   python manage.py runserver
   ```

## Usage
- **Sign up/Login** to create an account.
- **Follow Users** to see their articles.
- **Create New Articles** using the editor.
- **Like & Comment** on posts.
- **Manage Your Profile** and interact with the community.

## Project Structure
MYBLOG/
│-- articles/            # App for managing blog articles
│   ├── migrations/      # Database migrations
│   ├── models.py        # Database models for articles
│   ├── views.py         # Views for handling article requests
│   ├── urls.py          # URL routing for articles
│   ├── templates/       # Templates related to articles
│-- likes_comments/      # App for handling likes & comments
│   ├── models.py        # Models for likes & comments
│   ├── views.py         # Views for handling interactions
│   ├── urls.py          # URL routing for likes & comments
│-- media/               # Storage for uploaded media files
│-- myblog/              # Main Django project configuration
│   ├── settings.py      # Project settings
│   ├── urls.py          # Main URL configurations
│   ├── wsgi.py          # WSGI entry point
│   ├── asgi.py          # ASGI entry point
│-- templates/           # Global HTML templates
│-- user_auth/           # User authentication app
│   ├── models.py        # User authentication models
│   ├── views.py         # Views for login/logout/signup
│   ├── urls.py          # URL routing for authentication
│-- user_profile/        # User profile management app
│   ├── models.py        # Profile model
│   ├── views.py         # Views for user profile
│   ├── urls.py          # URL routing for profiles
│-- db.sqlite3           # SQLite database file
│-- manage.py            # Django management script


## Contributing
Feel free to contribute! Fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License.

---
Happy Coding! 🚀

