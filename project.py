import math

def menu():
    print("\n==============================")
    print("        PYTHON MATH LAB")
    print("==============================")
    print("1. Calculator")
    print("2. Graph")
    print("3. Exit")
    print("==============================")


# ---------- Calculator Functions ----------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def calculator():
    print("\n--- Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Percentage")

    choice = input("Choose an operation: ")

    try:
        a = float(input("Enter first number: "))

        if choice == "6":
            b = float(input("Enter percentage: "))
            result = a * b / 100
            print(f"Result: {result}")
            return

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid operation.")
            return

        b = float(input("Enter second number: "))

        if choice == "1":
            result = add(a, b)
            symbol = "+"

        elif choice == "2":
            result = subtract(a, b)
            symbol = "-"

        elif choice == "3":
            result = multiply(a, b)
            symbol = "*"

        elif choice == "4":
            if b == 0:
                print("Cannot divide by zero.")
                return

            result = divide(a, b)
            symbol = "/"

        else:
            result = power(a, b)
            symbol = "^"

        print(f"Result: {a} {symbol} {b} = {result}")

    except ValueError:
        print("Please enter valid numbers.")


# ---------- Graph Functions ----------

def linear(x):
    return x

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def root(x):
    return math.sqrt(abs(x))

def choose_function():
    functions = {
        "1": ("y = x", linear),
        "2": ("y = x²", square),
        "3": ("y = x³", cube),
        "4": ("y = sin(x)", sine),
        "5": ("y = cos(x)", cosine),
        "6": ("y = √|x|", root)
    }

    print("\n--- Graphing Calculator ---")
    print("1. y = x")
    print("2. y = x²")
    print("3. y = x³")
    print("4. y = sin(x)")
    print("5. y = cos(x)")
    print("6. y = √|x|")

    choice = input("Choose a function: ")

    if choice not in functions:
        print("Invalid function.")
        return

    try:
        limit = int(input("Enter graph range (2-10): "))

        if limit < 2 or limit > 10:
            print("Range must be between 2 and 10.")
            return

        name, function = functions[choice]
        graph(function, name, limit)

    except ValueError:
        print("Please enter a whole number.")

def graph(function, name, limit):
    width = 41
    height = 15

# Calculate x values from -limit to +limit
    x_values = []

    for i in range(width):
        x = -limit + (2 * limit * i / (width - 1))
        x_values.append(x)

# Calculate y values
    y_values = []

    for x in x_values:
        try:
            y = function(x)

            if math.isfinite(y):
                y_values.append(y)
            else:
                y_values.append(None)

        except (ValueError, OverflowError):
            y_values.append(None)

# Get valid y values
    valid_values = []

    for y in y_values:
        if y is not None:
            valid_values.append(y)

    if not valid_values:
        print("Unable to graph this function.")
        return

    y_min = min(valid_values)
    y_max = max(valid_values)

# Make sure zero is included in the graph
    y_min = min(y_min, 0)
    y_max = max(y_max, 0)

# Prevent division by zero
    if y_min == y_max:
        y_min -= 1
        y_max += 1

# Position of x = 0
    zero_x = round(
        (0 - (-limit)) / (2 * limit) * (width - 1)
    )

# Position of y = 0
    zero_y = round(
        (y_max - 0) / (y_max - y_min) * (height - 1)
    )

    print(f"\n{name}")
    print()

# Draw the graph
    for row in range(height):

        line = ""

        for column in range(width):

# Calculate the mathematical y value for this row
            graph_y = y_max - (
                row * (y_max - y_min) / (height - 1)
            )

            value = y_values[column]

# Check whether the function passes through this position
            point = False

            if value is not None:
                difference = abs(value - graph_y)
                step = (y_max - y_min) / (height - 1)

                if difference <= step / 2:
                    point = True

# Draw function point
            if point:
                line += "●"

# Origin
            elif column == zero_x and row == zero_y:
                line += "┼"

# Y-axis
            elif column == zero_x:
                line += "│"

# X-axis
            elif row == zero_y:
                line += "─"

            else:
                line += " "

# Display y-axis value
        y_label = y_max - (
            row * (y_max - y_min) / (height - 1)
        )

        print(f"{y_label:7.2f}  {line}")

# X-axis label
    print(" " * 9 + "↑")
    print(" " * (zero_x + 9) + "x = 0")

    print()
    print(
        f"{' ' * 9}"
        f"{-limit:<8}"
        f"{0:^{width - 16}}"
        f"{limit:>8}"
    )
    print(" " * (width + 8) + "→ x")

def main():
    while True:
        menu()

        choice = input("Choose an option: ")

        if choice == "1":
            calculator()

        elif choice == "2":
            choose_function()

        elif choice == "3":
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
