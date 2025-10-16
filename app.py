store_items = [
    {"name": "Apple", "price": 0.99, "category": "Fruit"},
    {"name": "Bread", "price": 2.49, "category": "Bakery"},
    {"name": "Milk", "price": 1.99, "category": "Dairy"},
    {"name": "Eggs", "price": 3.49, "category": "Dairy"},
    {"name": "Water", "price": 4.99, "category": "Beverage"}
]



print(" Welcome to the store! Here's what's in stock:")
for index, item in enumerate(store_items):
    print(f"{index}: {item['name']} - ${item['price']} ({item['category']})")


choice = int(input(" Enter the index of the item you want to purchase: "))
selected_item = store_items[choice]
print(f"\n You purchased: {selected_item['name']}")


cart = []
total = 0


print("\n Let's keep shopping!")


while True:
    print("\nAvailable items:")
    for index, item in enumerate(store_items):
        print(f"{index}: {item['name']} - ${item['price']} ({item['category']})")


    choice = int(input("Enter the index of the item you want to purchase: "))
    selected_item = store_items[choice]
    cart.append(selected_item)
    total += selected_item["price"]
    print(f" Added {selected_item['name']} to your cart.")


    continue_shopping = input(" Do you want to continue shopping? (Yes/No): ")
    if continue_shopping != "Yes":
        break


print("\n Shopping Summary:")
for item in cart:
    print(f"- {item['name']}")
print(f" Total: ${total:.2f}")
