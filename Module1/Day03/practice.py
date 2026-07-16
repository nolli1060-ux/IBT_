# Unique cities
print("--- Unique cities ---")
cities = ["Addis Ababa", "Jimma", "Adama", "Jimma", "Hawassa", "Bahir Dar", "Addis Ababa"]
unique_cities = list(set(cities))
print(unique_cities)
print(len(unique_cities))
print()

# Price 
print("--- Price ---")
grocery_prices = {
    "Injera": 25,
    "Teff": 120,
    "Coffee": 1200,
    "Banana": 60,
    "Milk": 70
}
for item, price in grocery_prices.items():
    print(item, price)
print()


# Tax
print("--- Tax ---")
prices = [100, 250, 400,80]

prices_with_tax = [price * 1.15 for price in prices]
print(prices_with_tax)
print()

# Cheap items
print("--- Cheap items ---")
cheap_prices = [price for price in prices if price < 200]
print(cheap_prices)
print()

print("--- Write and Read ---")
# Write to a file
f = open("names.txt", "w")
f.write("Mati\n")
f.write("Ezana\n")
f.write("Nati\n")
f.close()

# Read from a file
f = open("names.txt", "r")
for line in f:
    print(line.strip())
f.close()
print()

# Safe division
print("--- Safe division ---")
try:
    user_input = input("Enter a number")
    number = float(user_input)
    result = 1000 / number
    print(result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")