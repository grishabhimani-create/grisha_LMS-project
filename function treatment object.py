# Data Analyzer and Transformer Program

data = []


def input_data():
    """Store user input data into a list."""
    global data

    numbers = input("Enter data for a 1D array (separated by spaces): ")

    data = list(map(int, numbers.split()))

    print("\nData has been stored successfully!")


def display_summary():
    """Display summary using built-in functions."""

    if len(data) == 0:
        print("No data available!")
        return

    print("\nData Summary:")
    print("- Total elements:", len(data))
    print("- Minimum value:", min(data))
    print("- Maximum value:", max(data))
    print("- Sum of all values:", sum(data))
    print("- Average value:", round(sum(data) / len(data), 2))


def factorial(n):
    """Calculate factorial using recursion."""

    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def calculate_factorial():
    """Take input and display factorial."""

    num = int(input("Enter a number to calculate its factorial: "))

    print(f"\nFactorial of {num} is: {factorial(num)}")


def filter_data():
    """Filter data using lambda function."""

    if len(data) == 0:
        print("No data available!")
        return

    threshold = int(input("Enter a threshold value: "))

    filtered = list(filter(lambda x: x >= threshold, data))

    print(f"\nFiltered Data (values >= {threshold}):")

    if filtered:
        print(*filtered, sep=", ")
    else:
        print("No values found")


def sort_data():
    """Sort data in ascending or descending order."""

    if len(data) == 0:
        print("No data available!")
        return

    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sorted_data = sorted(data)

        print("\nSorted Data in Ascending Order:")
        print(*sorted_data, sep=", ")

    elif choice == 2:
        sorted_data = sorted(data, reverse=True)

        print("\nSorted Data in Descending Order:")
        print(*sorted_data, sep=", ")

    else:
        print("Invalid choice!")


def dataset_statistics():
    """Return multiple dataset statistics."""

    if len(data) == 0:
        print("No data available!")
        return

    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = round(total / len(data), 2)

    return minimum, maximum, total, average


def display_statistics():
    """Display returned multiple values."""

    result = dataset_statistics()

    if result:
        minimum, maximum, total, average = result

        print("\nDataset Statistics:")
        print("- Minimum value:", minimum)
        print("- Maximum value:", maximum)
        print("- Sum of all values:", total)
        print("- Average value:", average)


# Main Program

while True:

    print("\nWelcome to the Data Analyzer and Transformer Program")

    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = int(input("\nPlease enter your choice: "))

    if choice == 1:
        input_data()

    elif choice == 2:
        display_summary()

    elif choice == 3:
        calculate_factorial()

    elif choice == 4:
        filter_data()

    elif choice == 5:
        sort_data()

    elif choice == 6:
        display_statistics()

    elif choice == 7:
        print("\nThank you for using the Data Analyzer and Transformer Program.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
