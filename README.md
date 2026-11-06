# CustomTkinter Simple Calculator

A desktop calculator built with Python and CustomTkinter.

## Features

- Addition, subtraction, multiplication, and division.
- Decimal number input.
- Clear and delete controls.
- Error messages for invalid expressions and division by zero.

## Technologies

- Python
- CustomTkinter
- AST (Abstract Syntax Trees)
- CTkMessagebox

## How It Works

The calculator takes an expression entered through the graphical interface, parses it using Python's `ast` module, and evaluates supported arithmetic operations through a custom recursive function.

It uses AST-based expression evaluation instead of Python's `eval()` function.

## Installation and Usage

1. Clone this repository.
2. Install the required dependencies:

   `pip install customtkinter CTkMessagebox`

3. Run the application:

   `python "simple calculator.py"`

## About

This project explores Python GUI development, event-driven programming, widget management, and basic expression evaluation.
