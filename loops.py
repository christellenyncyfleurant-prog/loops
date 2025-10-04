# Taco Tuesday Program

def print_menu():
    print("\nTaco Palace Menu")
    print("1. Taco - $2.50")
    print("2. Burrito - $3.50")
    print("3. Nachos - $4.00")
    print("4. Soft Drink - $1.95")
    print("5. Quit")

def get_price(choice):
    if choice == 1:
        return 2.50
    elif choice == 2:
        return 3.50
    elif choice == 3:
        return 4.00
    elif choice == 4:
        return 1.95
    else:
        return 0.0

food_items = ["Taco", "Burrito", "Nachos", "Soft Drink"]

order = []
total = 0.0
choice = 0

print("Welcome to Taco Palace! Please view the menu below and make a selection.")

while choice != 5:
    print_menu()
    choice = int(input("Enter your selection: "))

    if 1 <= choice <= 4:
        item = food_items[choice - 1]
        price = get_price(choice)
        order.append(item)
        total += price
        print("You selected a", item)

print("\nYou ordered:", ", ".join(order))
print("Your total is $", round(total, 2))
