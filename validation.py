import validators

email = "Ajay@gmail.com"
print(f"--->{type(validators.email(email))}")
if validators.email(email):
    print("yes")
else:
    print("No")