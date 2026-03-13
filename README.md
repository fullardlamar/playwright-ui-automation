# Playwright UI Automation Framework

This project is a UI automation testing framework built with **Python**, **Playwright**, and **PyTest** using the **Page Object Model (POM)** design pattern.

It automates core user workflows on the Sauce Demo sample application and demonstrates a structured test automation framework suitable for portfolio and resume use.

## Features

- Automated login validation
- Automated add-to-cart flow
- Automated end-to-end checkout completion flow
- Reusable page objects for maintainability
- Centralized test data in a configuration file
- Version controlled with Git and GitHub

## Project Structure

```text
playwright-ui-automation
├── pages
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests
│   ├── test_login.py
│   └── test_checkout.py
├── utils
│   ├── __init__.py
│   └── config.py
├── .gitignore
└── README.md
