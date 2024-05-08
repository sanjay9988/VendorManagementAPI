# Vendor Management API

This repository contains the Vendor Management API, which allows users to manage vendors within their system. The API is built using Django and Django REST framework.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/vendor-management-api.git
   ```

2. Navigate to the project directory:
   ```bash
   cd vendor-management-api
   ```

3. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # for Unix/Mac
   .\env\Scripts\activate  # for Windows
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

The API will be accessible at `http://localhost:8000/`.

## API Endpoints

https://documenter.getpostman.com/view/34269375/2sA3JJAids

## Authentication

Implemetation is in progress :
   ```
   Authorization: Token your_token_here will be implemented.
   ```

## Dependencies

- asgiref==3.8.1
- Django==5.0.4
- django-filter==24.2
- djangorestframework==3.15.1
- sqlparse==0.5.0
- typing_extensions==4.11.0
- uuid==1.30

## POSTMAN API DOCUMENTATION 
https://documenter.getpostman.com/view/34269375/2sA3JJAids

## License

This project is licensed under the MIT License
