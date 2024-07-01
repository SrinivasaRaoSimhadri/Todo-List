# To-Do List Web Application

## Overview

This is a web-based To-Do List application built using Django and Bootstrap. The application allows users to manage their tasks efficiently by adding, editing, deleting, and searching tasks. It also includes user authentication for a personalized experience.

## Features

- **User Authentication**: Secure login and logout functionality.
- **Task Management**:
  - Add new tasks
  - Edit existing tasks
  - Delete tasks
  - Mark tasks as completed
- **Search Functionality**: Easily find tasks by keywords.
- **Responsive Design**: Built with Bootstrap for a mobile-friendly experience.

## Technologies Used

- **Backend**: Django
- **Frontend**: Bootstrap, HTML, CSS
- **Database**: SQLite (default with Django)

## Setup and Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/SrinivasaRaoSimhadri/Todo-List.git
    cd Todo-List
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

4. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

5. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

6. Open your web browser and go to `http://127.0.0.1:8000` to see the application.

## Usage

1. **Register or login**: Create a new account or log in with an existing account.
2. **Add a task**: Click on the "Add Task" button and fill out the form.
3. **Edit or delete tasks**: Use the edit and delete buttons next to each task.
4. **Search tasks**: Use the search bar to find specific tasks.


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.


Thank you for checking out my project! 😊
