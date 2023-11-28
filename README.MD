# Bank security console

This is an internal repository for Shine Bank employees. If you're in this repository by accident, you won't be able to run it because you don't have access to the database, but you can freely use the layout code or see how to database queries are implemented.
Security desk is a site that can be connected to a remote database with business cards and badge cards of our bank employees.

## Installation

1. Clone the repository to your computer:
    ```
    git clone https://github.com/barseeek/django-orm-watching-storage.git
    ```
2. Navigate to the project directory:
    ```
    cd django-orm-watching-storage
    ```
3. Install the necessary dependencies (Python3 should be already installed):
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Create a `.env` file in the project's root directory and add the required environment variables:
    ```
    DATABASE_HOST=YOUR_DATABASE_HOST
    DATABASE_USERNAME=YOUR_DATABASE_USERNAME
    DATABASE_PASSWORD=YOUR_DATABASE_PASSWORD
    SECRET_KEY=YOUR_SECRET_KEY
    DEBUG=TRUE_OR_FALSE
    ```
2. Run the script to run the website locally:
    ```
    python manage.py runserver 0.0.0.0:8000
    ```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).