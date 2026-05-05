# Fundamentel Booster - Interactive Personal Data Collector

#=========Welcome Section===========

print("welcome to the Interactive Personal Data Collector!")

print("\n This will collect your personal information.")

print("\n perform some calculation , and show you data type datails.")

print("\n Let's get started!!!")

#========collect information section========


print("="*50)

name = input ("Please Enter your name:")

age_str = input("please Enter Your age:")

age = int(age_str)

height = float(height_str)

fav_num_str = input("Pease Enter Your Favourite number:")

fav_num = int(fav_num_str)

#========= data processing==========

print("\n"+"="*50)

print("processing your data............")
print("="*50)

# calculate birth year

cur_year = 2026

birth_year = cur_year_age

# calculate height to centimeter

height_cm = height*100


# perform some arithmetic operation

sum_value = age*fav_num

product_value = age*fav_num

# Type conversion

height_as_int = int(height)

age_as_float(age)

age_as_string = str(age)

# display result

print("\n"+"="*50)

print("Thank you! you have is the information we collected:")

print("="*50)

# display each variable with its tyoe and memory address

print(f"\n Variable Details:")

print(f"name:{name}->{type:(name)}->Address:{id(name)}")

print(f"age:{age} -> {type:(age)} -> Address:{id(age)}")

print(f"height:{height} -> {type:(height)} -> address:{id(height)}")

print(f"favourite number:{fav_num}->{type:(fav_num)}->address:{id(fav_num)}")

#=======display conversion=======

print("="*50)

print("type conversion")

print("="*50)

print(f"\nHeight as integer:{height_as_int}")

print(f"\nAge as float:{age_as_float}")

print(f"\nAge as string:{age_as_string}")

#========display operation=========

print("="*50)

print("calulated results:")

print("="*50)

print(f"\n your height in centimeter:{height_cm}cm")

print(f"Approximately! your birth year:{birth_year}")

print(f"\n Sum of year age and favorite number:{sum_value}")

print(f"\n Product of your age and favourite number:{product_value}")

# string contination

greeting = "Hello","+name+""!"

message = f"your Favourite number is{fav_num}"

print(f"->'{greeting}'")

print(f"->type:{type(greeting)}")

print(f"->address:{id(greeting)}")

print(f"->'{message}'")

print(f"->type:{type(message)}")

print(f"->address:{id(message)}")

#=======Summary Table========

print("="*50)

print("summary Table:")

print("="*50)

print(f"\n{'variable':<20}{'value':<20}{'type':<25}{'id':<15}")

print(f"\n{'name':<20}{str(name):<20}{str(type(name)):<25}{id(name):<15}")

#===========closing message========

print("="*50)

print("Thank you for using the personal data collection!!")

print("="*50)

print("\n You've successfully explore:")

print("\n input()and print() functions")

print("\n String,integer and Float data types")

print("\n Arithmetic Operation(+,-,*,/).")

print("type() and id() built-in functions")

print("string concatination")

print("type casting")

print("="*50)
