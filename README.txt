# Test Case Registrator

## Description

Test Case Registrator is a simple Python application designed to help a test team create, register, and manage test cases in one place.

The purpose of the application is to make it easier to organize test cases and access previously registered information. 
Users interact with the program through a text-based menu where they can choose between the available functions.

The program provides two main features:

- **Create a test:** Allows users to register a new test case by entering the required information.
- **View test cases:** Displays all previously registered test cases.

Each test case contains the following information:

- **Test Case Title:** The name or title of the test case.
- **Purpose:** A description of what the test case is intended to verify.
- **Expected Result:** Describes the expected outcome when the test is performed.

## Program Structure

The application is developed using OOP and follows a simple structure that separates responsibilities between different classes.

The system consists of the following main components:

- **TestCase (Model):** Represents an individual test case and contains its title, purpose, and expected result. It acts as a data model for the information registered by the user.
- **TestCaseService (Service):** Handles the application's business logic. It manages the creation of new test cases and retrieves existing test cases by communicating with the repository.
- **TestCaseRepository (Repository):** Responsible for storing and retrieving test cases. The registered test cases are stored in a list in memory.

Additional components:

- **TestCaseDialog:** Handles user interaction through a text-based menu. It collects input from the user and presents the available options and registered test cases.
- **console_helper.py (Utils):** Contains reusable helper functions for console interaction. These include clearing the terminal screen, pausing program execution until the user presses enter, and validating that required user input is not empty.
- **main.py:** Acts as the entry point of the application and starts the program.

This structure separates user interaction, business logic, data representation, and data storage, making the application easier to understand, maintain, and develop further.

## Requirements

To run the application, you need:

- Python 3.10 or later.
- A terminal or code editor that supports Python.

No external libraries or additional packages are required.

## How to Run

1. Clone the GitHub repository or download the project files.
2. Open the project folder in your terminal or code editor.
3. Make sure Python 3.10 or later is installed.
4. Run the following command in the terminal:

   ```bash
   python main.py
   ```

5. Follow the instructions in the menu to create or view test cases.

## Storage

The application stores all registered test cases in memory using a Python list within the repository. No database, files, or external storage solutions are used. 
This means that test cases are only available while the application is running. When the program is closed, all registered test cases are lost.

## Limitations

The application is designed as a simple test case registration tool and has some limitations:

- Test cases cannot be saved permanently.
- Previously registered test cases cannot be accessed after restarting the application.
- The application does not support editing or deleting existing test cases.
- The program is designed for text-based interaction through the terminal.