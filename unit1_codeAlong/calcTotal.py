def calculate_total(price, quantity):
    total = price * quantity
    return total


def main():
    item_price = 15
    num_items = 3

    order_total = calculate_total(item_price, num_items)

    print("Total:", order_total)


if __name__ == "__main__":
    main()