# We ask the user for the number of items they want to buy
num_items = int(input("Enter the number of items you want to buy: "))

if num_items > 3:
    print("Discount applied")
else:
    print("No discount")