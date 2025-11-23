def practice_1():
    """
    Practice!

    uncomment the lines and print out the results below
    """
    print("PRACTICE 1")
    print("----------")

    result_1 = 17 / 3
    # try printing f"{result_1:.2f}" and observe the difference
    print(f"17 divided by 3 is {result_1}\n")

    result_2 = 17 // 3
    print(f"17 floor divided by 3 is {result_2}\n")

    result_3 = 17 % 3
    print(f"The remainder of 17 divided by 3 is {result_3}\n")

    result_4 = 5 * 3 + 2
    print(f"Altogether, 5 * 3 + 2 is {result_4}\n")
    print(f"Altogether, {result_2} * 3 + {result_3} is {result_4}\n")


def practice_2(item_price, quantity):
    """
    Magic numbers?
    """
    print("PRACTICE 2")
    print("----------")

    SALES_TAX_RATE = 0.06
    FLAT_SHIPPING_FEE = 5.0

    subtotal = item_price * quantity
    subtotal += subtotal * SALES_TAX_RATE + FLAT_SHIPPING_FEE
    print(
        f"Subtotal for item with unit price {item_price} and quantity {quantity} is {subtotal}."
    )


def practice_3(item_price, quantity, discount=0.1):
    """
    Add a 10% discount to the price BEFORE shipping fees
    """
    print("PRACTICE 3")
    print("----------")

    SALES_TAX_RATE = 0.06
    FLAT_SHIPPING_FEE = 5.0

    subtotal = item_price * quantity
    subtotal += subtotal * SALES_TAX_RATE
    subtotal *= discount
    subtotal += subtotal * FLAT_SHIPPING_FEE
    print(
        f"Subtotal for item with unit price {item_price} and quantity {quantity} is {subtotal}."
    )


def main():
    practice_1()
    practice_2(item_price=20.00, quantity=5)
    practice_3(item_price=10.00, quantity=2)


if __name__ == "__main__":
    main()
