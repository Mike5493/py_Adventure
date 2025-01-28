#==============================================
#   * Inventory System for managing items.
#==============================================
#   * Author: Mikey
#   * Date: 01/25/2025
#==============================================

inventory = []
MAX_ITEMS = 10

#====Display Inventory====
def show_inventory():
    if inventory:
        print("\nYour inventory contains:")
        for index, (item, count) in enumerate(inventory, start=1):
            print(f"{index}. {item} (x{count})")
        else:
            print("\nYour inventory is empty!")
        print("~" * 30)

def add_item(item):
    global inventory
    total_items = sum(count for _, count in inventory)
    if total_items >= MAX_ITEMS:
        print("\nYour inventory is full..do you need to drop anything?")
        print("~" * 30)
        return
    
    for i, (inv_item, count) in enumerate(inventory):
        if inv_item == item:
            inventory[i] = (inv_item, count + 1)
            print(f"You picked up another {item}. (x{count + 1})")
            print("~" * 30)
            return
        
    inventory.append((item, 1))
    print(f"\nYou have picked up: {item} (x1)")
    print("~" * 30)


def remove_item(item):
    global inventory
    for i, (inv_item, count) in enumerate(inventory):
        if inv_item == item:
            if count > 1:
                inventory[i] = (inv_item, count - 1)
                print(f"\nYou dropped one {item}. (x{count -1})")
            else:
                inventory.pop(i)
                print(f"\nYou dropped: {item}")
            print("~" * 30)
            return
        print(f"\n{item} isn't in your inventory!")
        print("~" * 30)


def has_item(item):
    return any(inv_item == item for inv_item, _ in inventory)

#=====================
#   Welcome Message
#=====================
print("Get ready..choose an item.")
invalid_attempts = 0
while True:
    print("\nOptions:")
    print("1. Show Inventory")
    print("2. Pick up item")
    print("3. Drop Item")
    print("4. Check for Item")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")
    print("~" * 30)

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
        print("~" * 30)
        invalid_attempts = 0
    elif choice == "5":
        print("\nBye, for now..")
        print("~" * 30)
        break
    else:
        invalid_attempts += 1
        print(f"\nWrong choice..you have {3 - invalid_attempts} attempts left.")
        print("~" * 30)
        if invalid_attempts >= 3:
            print("\nYou reached your limit..see ya!")
            print("~" * 30)
            break
        