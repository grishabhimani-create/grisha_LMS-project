# Personal Journal Manager (File Operator Project)

import os
from datetime import datetime

FILE_NAME = "journal.txt"


# Add Entry
def add_entry():
    entry = input("\nEnter your journal entry:\n")

    with open(FILE_NAME, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}]\n")
        file.write(entry + "\n\n")

    print("Entry added successfully!")


# View All Entries
def view_entries():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.read()

            if data.strip() == "":
                print("No journal entries found. Start by adding a new entry!")
            else:
                print("\nYour Journal Entries:")
                print("-" * 35)
                print(data)

    except FileNotFoundError:
        print("No journal entries found. Start by adding a new entry!")


# Search Entry
def search_entry():
    keyword = input("\nEnter a keyword or date to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            data = file.read()

            if keyword.lower() in data.lower():
                print("\nMatching Entries:")
                print("-" * 35)

                entries = data.split("\n\n")

                found = False
                for entry in entries:
                    if keyword.lower() in entry.lower():
                        print(entry)
                        print()
                        found = True

                if not found:
                    print(f"No entries were found for the keyword: {keyword}")

            else:
                print(f"No entries were found for the keyword: {keyword}")

    except FileNotFoundError:
        print("Error: The journal file does not exist. Please add a new entry first.")


# Delete All Entries
def delete_entries():
    if not os.path.exists(FILE_NAME):
        print("No journal entries to delete.")
        return

    choice = input(
        "\nAre you sure you want to delete all entries? (yes/no): "
    ).lower()

    if choice == "yes":
        open(FILE_NAME, "w").close()
        print("All journal entries have been deleted.")
    else:
        print("Deletion cancelled.")


# Main Menu
while True:
    print("\n" + "=" * 40)
    print("Welcome to Personal Journal Manager!")
    print("Please select an option:")
    print("\n1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    try:
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            add_entry()

        elif choice == 2:
            view_entries()

        elif choice == 3:
            search_entry()

        elif choice == 4:
            delete_entries()

        elif choice == 5:
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break

        else:
            print("Invalid option. Please select a valid option from the menu.")

    except ValueError:
        print("Please enter a valid number.")
