store_items = [
    {"name": "Yeezy Slides Onyx", "price": 75.0, "category": "Adidas"},
    {"name": "Yellow Crocs", "price": 50.0, "category": "Crocs"},
    {"name": "Yeezy 360", "price": 110.75, "category": "Adidas"},
    {"name": "Jordan 1s", "price": 120.50, "category": "Jordan"},
    {"name": "Air Force 1s", "price": 75.0, "category": "Nike"}
]



print(" Welcome to the store! Here's what's in stock:")
for index, item in enumerate(store_items):
    print(f"{index}: {item['name']} - ${item['price']} ({item['category']})")


choice = int(input(" Enter the index of the item you want to purchase: "))
selected_item = store_items[choice]
print(f"\n You purchased: {selected_item['name']}")


cart = []
total = 0


print("\n Sorry I didn't recieve your order! Please enter again, Thank You!")


while True:
    print("\nAvailable items:")
    for index, item in enumerate(store_items):
        print(f"{index}: {item['name']} - ${item['price']} ({item['category']})")


    choice = int(input("Enter the index of the item you want to purchase: "))
    selected_item = store_items[choice]
    cart.append(selected_item)
    total += selected_item["price"]
    print(f" Added {selected_item['name']} to your cart.")


    continue_shopping = input(" Do you want to continue shopping? (yes/no): ")
    if continue_shopping != "yes":
        break


print("\n Shopping Summary:")
for item in cart:
    print(f"- {item['name']}")
print(f" Total: ${total:.2f}")
