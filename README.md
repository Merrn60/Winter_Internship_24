# Winter Internship 2025 - HR System and Python Scripts

This repository contains two main components developed during the Winter Internship 2025: an **HR Management System** and a collection of **Python scripts** for digit manipulation. Below is an overview of each component, their functionality, and usage instructions.

## Repository Contents

### 1. HR Management System
The HR Management System is a Python-based application for managing employees, departments, and projects within an organization. It includes classes to handle employee details, department assignments, and project allocations.

#### Files
- **`main.py`**: Entry point for the HR system, demonstrating the creation and management of employees, departments, and projects.
- **`employee.py`**: Defines the `Employee` class with methods for managing employee details and project assignments.
- **`department.py`**: Defines the `Department` class for managing department details and employee assignments.
- **`project.py`**: Defines the `Project` class for managing project details, budgets, deadlines, and assigned employees.
- **`hr_system.py`**: Defines the `HRSystem` class to manage collections of employees, departments, and projects.

#### Functionality
- Create and manage employee records (ID, name, position, salary, projects).
- Organize employees into departments with assigned managers.
- Create and track projects with budgets, deadlines, and assigned employees.
- Display details of employees, departments, and projects.

#### Usage
1. Ensure all HR system files (`main.py`, `employee.py`, `department.py`, `project.py`, `hr_system.py`) are in the same directory.
2. Run `main.py` using Python (e.g., `python main.py`).
3. The script will output details of employees, departments, and projects as defined in `main.py`.

### 2. Python Digit Manipulation Scripts
This section contains a collection of Python scripts developed to perform various operations on numerical inputs, focusing on digit manipulation and basic computations. These scripts are stored in the `internship_scripts` directory.

#### Scripts
1. **`1stp.py`**: Converts each digit of an input number into its English word representation (e.g., "123" becomes "onetwothree").
2. **`2nd.py`**: Counts the occurrences of a specific digit in a given number and prints the count.
3. **`3rd.py`**: Calculates the sum of each digit raised to its own power (e.g., for "123", computes 1¹ + 2² + 3³).
4. **`4th.py`**: Checks if all digits in a number are unique, returning `True` if they are, and `False` otherwise.
5. **`5th.py`**: Computes the product of all digits in a given number.
6. **`6th.py`**: Checks if a specific digit exists in a number, returning `True` if found, and `False` otherwise.
7. **`7th.py`**: Sums the digits at even positions (0-based index) in a given number.
8. **`8th.py`**: Swaps the first and last digits of a number and prints the result.
9. **`9th.py`**: Finds the difference between the maximum and minimum digits in a number.
10. **`10th.py`**: Removes all occurrences of a specific digit from a number and prints the resulting string.

#### Usage
- Navigate to the `internship_scripts` directory.
- Run any script using Python (e.g., `python 1stp.py`).
- Follow the console prompts to input a number (and sometimes an additional digit).
- The scripts assume valid input (numeric strings). Ensure inputs are digits to avoid errors.

## Requirements
- **Python 3.x**
- No external libraries are required; all scripts use standard Python functionality.

## Notes
- The HR system and digit manipulation scripts are independent components. The HR system focuses on object-oriented programming, while the internship scripts emphasize string and digit manipulation.
- Error handling for invalid inputs (e.g., non-numeric characters) is not implemented in the internship scripts. Users should provide valid numeric strings.
- For detailed functionality, review the source code of each file.

## Repository Link
[Winter Internship 2025 Repository](https://github.com/Merrn60/Winter_Internship_24)

---
*This README provides an overview of the repository contents and usage instructions. For detailed functionality, review the source code of each script or module.*
