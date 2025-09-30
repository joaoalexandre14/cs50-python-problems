def main():
    price = 50  # total cost
    inserted = 0  # amount inserted 

    # Keep asking until enough money is inserted
    while inserted < price:
        print("Amount Due:", price - inserted)
        coin = int(input("Insert Coin: "))
        # Accept only 25, 10, 5
        if coin in [25, 10, 5]:
            inserted += coin

    # If more than 50 was inserted, return change
    print("Change Owed:", inserted - price)

if __name__ == "__main__":
    main()
