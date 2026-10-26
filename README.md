# Python Math Lab

#### Description:

Python Math Lab is a terminal-based mathematical tool written in Python. It combines a calculator with a graphing calculator, allowing users to perform common mathematical calculations and visualize mathematical functions directly in the terminal.

The project was created as my CS50P Final Project. I wanted to build something more useful than a basic calculator while keeping the program focused on Python concepts and techniques learned during the course.

When the program starts, it displays a menu with three options: Calculator, Graph, and Exit.

The Calculator supports addition, subtraction, multiplication, division, powers, and percentage calculations. It accepts decimal numbers and includes error handling for invalid numerical input and division by zero.

The Graphing Calculator allows the user to select from six mathematical functions:

* `y = x`
* `y = x²`
* `y = x³`
* `y = sin(x)`
* `y = cos(x)`
* `y = √|x|`

After selecting a function, the user enters a graph range from 2 to 10. The program calculates multiple points for the selected function and displays the function in the terminal using `●` characters. The graph also includes mathematical x and y axes, with the axes positioned according to the actual coordinates `x = 0` and `y = 0`.

The graphing system does not use an external plotting library. Instead, it calculates mathematical values and maps them to rows and columns in the terminal. This was one of the main challenges of the project because mathematical coordinates have to be converted into positions that can be displayed using text characters.

The project uses Python's built-in `math` module for mathematical operations such as sine, cosine, square root, and checking whether calculated values are finite.

The project is organized into two Python files.

`project.py` contains the complete application. It includes the main menu, calculator operations, graph functions, graph generation, input validation, and program control.

`test_project.py` contains automated tests written using `pytest`. The tests check the mathematical calculator functions as well as the menu, function selection, and graphing functionality.

One design decision I made was to keep the project in the terminal instead of creating a graphical user interface. This keeps the project focused on Python programming and makes the mathematical calculations and graph-generation logic the main features.

Another design decision was to avoid using `eval()` for mathematical expressions. Instead, the program provides a controlled set of mathematical functions. This makes the program safer and keeps its behavior predictable.

I also separated the calculator operations and graph functions into individual Python functions. This makes the code easier to understand, test, and maintain. For example, addition, subtraction, multiplication, division, and power each have their own function.

The project also includes error handling. Invalid numerical input is handled using `try` and `except`, while division by zero and invalid graph ranges are handled separately.

Overall, Python Math Lab combines mathematical calculations with terminal-based visualization in a single Python program. It demonstrates the use of functions, dictionaries, loops, lists, conditionals, exception handling, the `math` module, and automated testing in Python.

# By : Gushaan Mittal
