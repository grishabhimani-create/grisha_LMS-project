# logic box
def main(): 
    print("Welcome to the pattern generator and Number Analyzer !")

while True:
    print("\n Selector an option:")
    print("1.generate a pattern")
    print("2.Analyze a range of numbers")
    print("3.Exit")

    choice = input("Enter your choice:")

# option 1: pattern generation

if choice == '1':
    try:
        rows = int(input("Enter the number of rows for the pattern:"))
    except ValueError:
        print("Error: Please enter a valid integer number.")
        continue
        
    if rows <= 0 :
        print("Error: please enter a positive number of rows.")
        continue

    print("\npattern:")
    for i in range(1,rows + 1):
        for j in range(i):
            print("*",end=" ")
        print()

except valueError:

print("Invalid input ! please enter a valid integer.")

elif choice == '2':
    try:
        start = ("Enter the start of the range:")
        end = ("Enter the end of the range:")

if end < start:

print("Error : End of the range must be greater than or equal to the start.")

continue

total_sum = 0

for num in range(start, end + 1):
if num % 2 == 0:

print(f"number {num} is Even")

else:

print(f"number {num} is Odd")

total_sum += num

print(f"sum of all number from {start} to {end} is : {total_sum}")

except ValueError:
print("Invalid input! please enter valid integers.")

# option 3: Exit

elif choice == '3':
    print("Exiting the program. Goodbye!")
    break

else:
    print("Invalid choice! please select 1 , 2, or 3.")

if  _name_=="_main_":
    main()
