# Bank security console

The bank management console is designed to track passcards, people in the vault and staff member's visits

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
    DATABASE_PORT=YOUR_DATABASE_PORT
    DATABASE_NAME=YOUR_DATABASE_NAME
    DATABASE_USERNAME=YOUR_DATABASE_USERNAME
    DATABASE_PASSWORD=YOUR_DATABASE_PASSWORD
    SECRET_KEY=YOUR_SECRET_KEY
    DEBUG=TRUE_OR_FALSE
    ALLOWED_HOSTS=YOUR_ALLOWED_HOST1,YOUR_ALLOWED_HOST2...
    ```
2. Run the script to run the website locally:
    ```
    python manage.py runserver 0.0.0.0:8000
    ```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).