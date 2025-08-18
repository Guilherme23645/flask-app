# Flask User Profile App

A simple **Flask web application** that allows users to submit their information through a form and view their profile. The data is stored in a local **SQLite database**.

## Features

 - Home Page (`/`)
 - About Page (`/about/`)
 - User Form Validation (`/submit/`)
 - User Profile Page (`/user/<username>/`)
 - Data stored in SQLite (`users.db`)

## Requirements

 - Python 3.8+
 - Flask (Run `pip install flask`)
 - SQLite3 Database
   - `sudo <package-manager> install sqlite3` (Linux)
   - `brew install sqlite` (macOS)
   - Download from https://www.sqlite.org/download.html (Windows)
 - SQLite3 for Python (Bundled with Python)
 - SQLite Web (Optional, run `pip install sqlite_web`)

## Commands

### Initialize database

sqlite3 database/users.db < queries/schema.sql

### Run application

python3 index.py

### Online workbench (Optional)

sqlite_web database/users.db

## Coming Soon

 - Update user info function
 - Delete user function
 - Flashes for warning
