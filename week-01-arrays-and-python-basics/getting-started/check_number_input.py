# Prompts the user for input and checks if it's a number using isnumeric().
l = [1, 2, 3]

u = input("Give us a number, please!")

if u.isnumeric():
    print(f"Thank you for the number {u}")
else:
    print("Hey, why didn't you give us a number??")
