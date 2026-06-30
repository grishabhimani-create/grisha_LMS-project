# main.py

import datetime
import math
import random
import uuid
import file_operations


def explore_module():
    module = input("Enter module name (math, random, datetime, uuid): ")

    if module == "math":
        import math
        print(dir(math))

    elif module == "random":
        import random
        print(dir(random))

    elif module == "datetime":
        import datetime
        print(dir(datetime))

    elif module == "uuid":
        import uuid
        print(dir(uuid))

    else:
        print("Module not found.")


def main():

    while True:

        print("\n==============================")
        print("Welcome to Multi-Utility Toolkit")
        print("==============================")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate UUID")
        print("5. File Operations")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_module.menu()

        elif choice == "2":
            math_module.menu()

        elif choice == "3":
            random_module.menu()

        elif choice == "4":
            uuid_module.menu()

        elif choice == "5":
            file_operations.menu()

        elif choice == "6":
            explore_module()

        elif choice == "7":
            print("Thank you for using the toolkit!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
