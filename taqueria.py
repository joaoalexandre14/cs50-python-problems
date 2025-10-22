# Define the menu as a dictionary (with updated 2023 prices)
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Initialize the total order cost
total_cost = 0

# Infinite loop to receive orders
while True:
    try:
        # Prompt the user for an item and convert to title case
        item = input("Item: ").title()

        # Check if the item is on the menu
        if item in menu:
            # Add the item's price to the total
            total_cost += menu[item]
            # Print the current total, formatted to two decimal places
            print(f"Total: ${total_cost:.2f}")

    # Catch the EOFError that occurs when the user presses Ctrl-d
    except EOFError:
        # Print a newline for cleaner output and exit the program
        print()
        break
