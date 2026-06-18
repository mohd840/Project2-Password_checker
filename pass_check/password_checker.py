password = input("Enter your password:")

length = len(password)

special = "!@#$*_"

has_upper = False
has_lower = False
has_digit = False
has_specialchar = False


for char in password:

    if char.isupper():
        has_upper = True

    if char.islower():
        has_lower = True

    if char.isdigit():
        has_digit = True

    if char in special:
        has_specialchar = True


if length >= 12 and has_upper and has_lower and has_digit and has_specialchar:
    result = "Strong Password "
else:
    result = "Weak Password "


print(result)


with open("result.txt", "w") as file:
    file.write("Password Analysis Report\n")
    file.write("=======================\n\n")

    file.write(f"Password length: {length}\n")
    file.write(f"Contains uppercase: {has_upper}\n")
    file.write(f"Contains lowercase: {has_lower}\n")
    file.write(f"Contains numbers: {has_digit}\n")
    file.write(f"Contains special characters: {has_specialchar}\n\n")

    file.write(f"Final Result: {result}")
