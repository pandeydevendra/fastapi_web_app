FastAPI Web App

A simple FastAPI web application that provides a foundation for building and serving API endpoints with Python.


FastAPI
 is a modern, high-performance Python web framework for building APIs.

It provides:

Fast API performance
Automatic interactive API documentation
Python type hints and validation
Easy development and testing
Built-in support for asynchronous programming
Project Structure
gfastapi_web_app/
├── .gitignore
├── main.py
├── requirements.txt
└── README.md

Requirements

Make sure the following are installed on your system:

Python 3.9 or newer
pip
Git

You can check your Python installation from the terminal:

python --version


or:

python3 --version


Check pip:

pip --version


or:

pip3 --version

Setup

Clone the repository:

git clone https://github.com/USER.NAME/fastapi_web_app.git


Move into the project directory:

cd ~/fastapi

Create a Virtual Environment

It is recommended to use a Python virtual environment for the project.

On Linux/macOS:

python3 -m venv venv
source venv/bin/activate


On Windows PowerShell:

python -m venv venv
.\venv\Scripts\Activate.ps1


On Windows Command Prompt:

python -m venv venv
venv\Scripts\activate

Install Dependencies

Once the virtual environment is activated, install the required packages:

pip install -r requirements.txt

Run the FastAPI Application

Start the development server with:

uvicorn main:app --reload


If your system uses python3 and Uvicorn is installed as a Python module, you can also use:

python3 -m uvicorn main:app --reload


The application should start on:

http://127.0.0.1:8000


API Documentation

Swagger UI

Open:

http://127.0.0.1:8000/docs

ReDoc

Open:

http://127.0.0.1:8000/redoc


These interfaces allow you to explore and test available API endpoints directly from your browser.

Development

After making changes to the Python code, save the file. When running with:

uvicorn main:app --reload


the development server automatically reloads when it detects changes.

To stop the server:

Ctrl + C

Git Workflow

After making changes to the project:

git status


Stage the changes:

git add .


Create a commit:

git commit -m "Describe your changes"


Push the changes to GitHub:

git push

Current Status

This project is currently under development. The initial FastAPI application and project structure are in place.

License

This project is licensed under the MIT License. See the LICENSE file for details.