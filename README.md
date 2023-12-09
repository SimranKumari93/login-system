# Getting Started with Django

## Setup

1. **Clone the repository:**

    ```bash
    $ git clone https://github.com/myUserName/login-system.git
    $ cd login-system
    ```

2. **Create a virtual environment:**

    ```bash
    $ python -m venv venv
    ```

3. **Activate the virtual environment:**

    In VS Code type ctrl + Shift + P and Select Interpreter the select the one with '.\venv\Scripts\python.exe'. Restart the vscode terminal.

   Note: The `(venv)` in front of the prompt indicates that the virtual environment is active.

4. **Install dependencies:**

    ```bash
    (env)$ pip install -r requirements.txt
    ```

## Run the Application

1. **Run the Django development server:**

    ```bash
    (env)$ python manage.py runserver
    ```

3. **Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).**

Now, you should have the Django application up and running locally.

## Additional Notes

- Ensure that you have `git`, `python`, and `pip` installed on your system.
- Adjust commands if you're using a different version of Python (e.g., `python3` instead of `python`).
