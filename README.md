# Basic E-commerce Django App

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/Rahulns21/basic-ecommerce-django.svg)](https://github.com/Rahulns21/basic-ecommerce-django/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/Rahulns21/basic-ecommerce-django.svg)](https://github.com/Rahulns21/basic-ecommerce-django/issues)
[![GitHub forks](https://img.shields.io/github/forks/Rahulns21/basic-ecommerce-django.svg)](https://github.com/Rahulns21/basic-ecommerce-django/network)

## Overview

This is a basic e-commerce app built with Django, providing essential functionalities like user product browsing, shopping cart management, and a simple checkout process.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

Follow these steps to set up and run the app locally:

```bash
# Clone the repository
git clone https://github.com/Rahulns21/basic-ecommerce-django.git

# Navigate to the project directory
cd basic-ecommerce-django

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create a superuser (admin) account
python manage.py createsuperuser

# Run the development server
python manage.py runserver
