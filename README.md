# Gym-SpotFit
# 🏋️ SportFit - Age Based Gym Class System

This is a simple **Python program** that simulates a registration system for a gym called **SportFit**.  
The program asks the user for their **age** and, based on that age, assigns them to a **gym class**.

## 📌 Description

The program displays a welcome message and then asks the user to enter their age.  
Depending on the entered age, the system determines which training group the user belongs to.

### Class Classification

| Age | Class |
|-----|------|
| 13 or younger | Cannot enter |
| 14 - 17 | Youth class |
| 18 - 59 | General class |
| 60 or older | Senior class |

## 🧠 Logic Used

The program uses:

- `print()` to display messages
- `input()` to receive user data
- `int()` to convert the input value into a number
- Conditional statements `if`, `elif`, and `else`

These structures allow the program to evaluate different **age ranges**.

## 💻 Program Code

```python
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
```
