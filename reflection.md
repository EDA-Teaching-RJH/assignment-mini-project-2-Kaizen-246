# Developer Reflection

## Project Overview
I created a Python application called LabLog Manager or Labs n' Logs that allows users to add, view, and store experiment and fault entries. The system uses object-oriented programming, validation, file storage, and testing to demonstrate the concepts covered in lectures.

## Regular Expressions
I used regular expressions in the validators module to validate email addresses. I used the re.fullmatch function to ensure the entire string matches the required email format. Initially, I found regex difficult, but I simplified the pattern and tested both valid and invalid cases to ensure it worked correctly.

## Testing
I used the unittest framework to test my validation functions. I created test cases for both valid and invalid email inputs to ensure the function behaves correctly. This helped me understand how to verify that my code works under different conditions.

## Libraries
I used Python libraries such as re for regular expressions and csv for file handling. I also created my own custom library called lablog, which contains modules for models and validation. This helped organise the code and improve readability.

## File I/O
I implemented file I/O by saving user entries to a CSV file using Python’s csv module. This allows the data to be stored and accessed outside the program. This demonstrated my understanding of writing data to files.

## Object-Oriented Programming (OOP)
I used OOP by creating a base class called LogEntry and two subclasses called ExperimentEntry and FaultEntry. These subclasses inherit from the parent class and add their own attributes and methods. This shows my understanding of inheritance and class structure.

## Development Process
I built the project step by step using Git commits. I started with a simple script, then added classes, validation, a menu system, file saving, and testing. Breaking the project into smaller steps made it easier to debug and understand.

## Challenges
One challenge I faced was setting up the project structure correctly so that Python could import modules. I also had some difficulty with regex syntax, but I resolved this by testing patterns and simplifying the expressions.

## Conclusion
Overall, this project helped me understand how different programming concepts work together in a real application. I improved my skills in OOP, validation, file handling, and testing.