# Python Functions and Class Descriptions

## Description
This project involves creating a set of Python functions and a class that demonstrate fundamental programming concepts. Each function and the class are designed to perform specific tasks, such as mathematical operations, string manipulation, data sorting, dictionary merging, and object-oriented programming. The functions include basic operations like summing numbers, checking for even numbers, reversing strings, counting vowels, calculating factorials, and applying decorators. This project serves as a practical exercise in Python programming, reinforcing core skills essential for building more complex applications.

## Prerequisites
- Python Interpreter

- Code Editor or Integrated Development Environment (IDE)

- Command Line or Terminal:

## Getting Started

1.  Click on [this link](https://github.com/bmgwaro/python-week-1) in order to access the github repository containing this project.

2.  Click on fork to create copy of the repository.

3.  Open your terminal and navigate into the directory where you would like to save the work using the `cd` command.

         cd <directory_name>

4.  Copy and paste the following command in order to clone the repository into your local storage. Remember to replace `your_github_username` with your actual username.

         git clone git@github.com:your_github_username/python-week-1

5.  Navigate into the newly cloned folder and type in the `code .` command in order to open it on your text editor.

## Functions

1. **Function: `add_numbers`**  
   **Description:**  
   This function takes two parameters `num1` and `num2`, and returns their sum.

2. **Function: `is_even`**  
   **Description:**  
   This function takes a single parameter `number` and returns `True` if the number is even, and `False` otherwise.

3. **Function: `reverse_string`**  
   **Description:**  
   This function takes a string `text` as input and returns the reversed version of that string.

4. **Function: `count_vowels`**  
   **Description:**  
   This function takes a string `text` as input and returns the count of vowels (a, e, i, o, u) in the string, ignoring case sensitivity.

5. **Function: `calculate_factorial`**  
   **Description:**  
   This function takes a non-negative integer `n` as input and returns the factorial of that number.

6. **Function: `apply_decorator`**  
   **Description:**  
   This function takes another function `func` as input and applies a decorator named `decorator_func`. The decorator prints "Decorator Applied" before calling the original function.

7. **Function: `sort_by_age`**  
   **Description:**  
   This function takes a list of tuples, where each tuple contains a name and an age, and sorts the list by age in ascending order.

8. **Function: `merge_dicts`**  
   **Description:**  
   This function takes two dictionaries as input and merges them into a single dictionary. If there are any common keys, their values are summed up.

9. **Class: `Car`**  
   **Description:**  
   This class represents a car with attributes `make`, `model`, and `year`. It includes a method `display_info` that prints out the car's information.