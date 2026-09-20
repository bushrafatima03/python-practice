import getpass
password = getpass.getpass("Enter your password:")
print(len(password))
if len(password) < 8:
    print("Too short!")
elif len(password) <= 12:
    print("Correct length!")
else:
    print("Too long!")
has_number = False
for char in password:
    if char.isdigit():
        has_number = True
if has_number:
    print("Contains a number.")
else:
    print("No number found.")

has_uppercase = False
for char in password:
    if char.isupper():
        has_uppercase = True
if has_uppercase:
    print("Contains an uppercase alphabet.")
else:
    print("No uppercase alphabet found.")
has_lowercase = False
for char in password:
    if char.islower():
        has_lowercase = True
if has_lowercase:
    print("Contains an lowercase alphabet.")
else:
    print("No lowercase alphabet found.")
has_special = False
for char in password:
    if not char.isalnum():
        has_special= True
if has_special:
    print("Contains a Special character.")
else:
    print("No Special charactetr found.")
if (len(password) >= 8 and has_number and has_uppercase and has_special):
    print("Strong password!")
elif len(password) >= 6 and has_number:
    print("Medium password.")
else:
    print("Weak password.")
if not has_number:
    print("Add a number.")
if not has_uppercase:
    print("Add an uppercase alphabet.")
if not has_lowercase:
    print("Add a lowercase alphabet.")
if not has_special:
    print("Add a special character.")
if len(password) < 8:
    print("Make the password atleast 8 characters long.")