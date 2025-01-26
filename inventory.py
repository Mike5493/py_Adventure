#==============================================
#   * Inventory System for managing items.
#==============================================
#   * Author: Mikey
#   * Date: 01/25/2025
#==============================================

inventory = []

#====Display Inventory====
def show_inventory():
    if inventory:
        print("\nYour inventory contains:")
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item}")
        else:
            print("\nYour inventory is empty!")

def add_item(item):
    inventory.append(item)
    print(f"\nYou have picked up: {item}")

def remove_item(item):
    if item in inventory:
        inventory.remove(item)
        print(f"\nYou dropped: {item}")
    else:
        print(f"\n{item} isn't in your inventory!")

def has_item(item):
    return item in inventory

#=====================
#   Welcome Message
#=====================
print("Get ready..choose an item.")
while True:
    print("\nOptions:")
    print("1. Show Inventory")
    print("2. Pick up item")
    print("3. Drop Item")
    print("4. Check for Item")
    print("5. Quit")

    choice = input("Choose and option (1-5): ")

    if choice == "1":
        show_inventory()
    elif choice == "2":
        item = input("What would you like to pick up: ")
        add_item(item)
    elif choice == "3":
        item = input("What would you like to drop: ")
        remove_item(item)
    elif choice == "4":
        item = input("What are you looking for: ")
        if has_item(item):
            print(f"\nYes, you have {item} in your inventory.")
        else:
            print(f"\nNo, {item} isn't in your inventory.")
    elif choice == "5":
        print("\nBye, for now..")
        break
    else:
        print("\nWrong choice..try again??")
        