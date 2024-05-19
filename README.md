# Django Dashboard

This is a Django web application that displays company user statistics and the daily growth of user signups using data from JSON files.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Features

- Displays the total number of users per company.
- Shows the daily growth of the total number of users.
- Uses Django for the web framework and Matplotlib for plotting graphs.

## Requirements

- Python
- Django
- Pandas
- Matplotlib

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/enfurars/Django_Dashboard.git
    cd Django_Dashboard
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Load Initial Data**:
    ```bash
    python manage.py import_data
    ```

## Running the Project

1. **Start the Development Server**:
    ```bash
    python manage.py runserver
    ```

2. **Open the Application**:
    Open your web browser and go to `http://127.0.0.1:8000`.

## Usage

- The homepage displays a table with the total number of users per company.
- The homepage also shows a graph of the daily growth of user signups.
