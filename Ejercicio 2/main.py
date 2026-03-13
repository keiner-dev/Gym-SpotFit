print("Welcome to SportFit")
print("We offer classes according to your age")

person = int(input("Enter your age: "))

if person <= 13:
    print("You cannot enter")
elif person <= 17:
    print("You belong to the youth class")
elif person <=59:
    print("You belong to the general class")
else:
    print("You belong to the senior class")