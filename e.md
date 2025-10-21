
Dictionary Project
Michael Whalen
•
Sep 30
Learning Progress
•
10 points
MAKE SURE TO DOWNLOAD THE MARKDOWN FILE TO ACCOMPANY THIS

Repo: https://classroom.github.com/a/z-pmSNBe

Python Dictionary Project 2025.pdf
PDF

Enumerate and Dicts.md
Text
Your work
Assigned
Private comments
Class comments
### 🗂 What is a Dictionary in Python?

Think of a **dictionary** in Python like a backpack with lots of labeled pockets.

* Each **label** is called a **key**.
* Each **thing inside** the pocket is called a **value**.

For example:

```python
item = {
    "name": "Samsung 55\" 4K UHD TV",
    "price": 429.99,
    "department": "Televisions",
    "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."
}
```

Here:

* `"name"` is a key, and `"Samsung 55\" 4K UHD TV"` is its value.
* `"price"` is a key, and `429.99` is its value.
* `"department"` is a key, and `"Televisions"` is its value.

So this dictionary tells us **information about one Best Buy item**.



### 📋 What is `best_buy_items`?

* Instead of just one dictionary, you have a **list of dictionaries**.
* Each dictionary describes **one item** (TV, laptop, camera, etc.).
* All together, it’s like Best Buy’s mini-catalog inside Python.

---

### 🎯 How to Select Specific Properties

If you want **just the name** of the first item, you write:

```python
best_buy_items[0]["name"]
```

* `[0]` → means “the first item in the list” (because Python starts counting at 0).
* `["name"]` → means “look inside that dictionary and grab the name.”

So this prints:

```
Samsung 55" 4K UHD TV
```

If you want the **price** of the second item:

```python
best_buy_items[1]["price"]
```

---

### 🔢 What is `enumerate`?

Normally, when you loop over a list, you just get the items.
But sometimes you also want the **number** (the position in the list).

That’s what `enumerate` does: it gives you **both the index number AND the item**.

Example from your code:

```python
for index, item in enumerate(best_buy_items):
    print(index, ":", item["name"])
```

This does two things:

1. `index` → the position in the list (0, 1, 2, 3, …).
2. `item` → the dictionary at that position.

So the output looks like:

```
0 : Samsung 55" 4K UHD TV
1 : LG 65" OLED TV
2 : Sony Noise Cancelling Headphones
...
```

It’s like making a **numbered shopping list** automatically.

---

✅ **Summary for a middle schooler:**

* A dictionary is like a **labeled backpack pocket** (key = label, value = stuff inside).
* A list of dictionaries is like a **shopping catalog**.
* `["name"]` or `["price"]` lets you pull out a specific piece of info.
* `enumerate` is like saying: “Give me the item AND its number in line.”

---
