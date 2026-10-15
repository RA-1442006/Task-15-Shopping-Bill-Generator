# Shopping Bill Generator


def add_product():
    # get product name and check that it is not empty
    while True:
        name = input("Enter product name (or 'done' to finish): ").strip()
        if not name:
            print("Product name cannot be empty. Please try again.")
            continue
        if name.lower() == "done":
            return None
        break

    # get quantity and make sure it is a positive whole number
    while True:
        try:
            qty = int(input("Enter quantity: "))
            if qty <= 0:
                print("Quantity must be greater than zero. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid quantity. Please enter a valid whole number.")

    # get price and check that it is not negative
    while True:
        try:
            price = float(input("Enter price per unit: "))
            if price < 0:
                print("Price cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid price. Please enter a valid number.")

    return {
        "name": name,
        "quantity": qty,
        "price": price
    }


def calculate_subtotal(items):
    subtotal = 0.0
    for item in items:
        subtotal += item["quantity"] * item["price"]
    return subtotal


def calculate_discount(subtotal):
    # 10% discount if subtotal is 1000 or more
    if subtotal >= 1000:
        return subtotal * 0.10
    return 0.0


def calculate_tax(amount):
    # 18% GST on the amount after discount
    return amount * 0.18


def print_bill(items):
    if not items:
        print("\nNo items were added. No bill to generate.")
        return

    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    discounted_amount = subtotal - discount
    tax = calculate_tax(discounted_amount)
    final_amount = discounted_amount + tax

    print("\n" + "=" * 52)
    print("SHOPPING BILL".center(52))
    print("=" * 52)
    print(f"{'Item':<22}{'Qty':<6}{'Price':<12}{'Total':<12}")
    print("-" * 52)

    for item in items:
        line_total = item["quantity"] * item["price"]
        price_str = f"Rs. {item['price']:.2f}"
        total_str = f"Rs. {line_total:.2f}"
        print(f"{item['name']:<22}{item['quantity']:<6}{price_str:<12}{total_str:<12}")

    subtotal_str = f"Rs. {subtotal:.2f}"
    discount_str = f"Rs. {discount:.2f}"
    tax_str = f"Rs. {tax:.2f}"
    final_str = f"Rs. {final_amount:.2f}"

    print("-" * 52)
    print(f"{'Subtotal:':<37}{subtotal_str:>15}")
    print(f"{'Discount:':<37}{discount_str:>15}")
    print(f"{'Tax (18% GST):':<37}{tax_str:>15}")
    print("=" * 52)
    print(f"{'Final Amount:':<37}{final_str:>15}")
    print("=" * 52)


def main():
    print("=== Shopping Bill Generator ===")
    items = []

    while True:
        product = add_product()
        if product is None:
            break
        items.append(product)
        print(f"Added '{product['name']}' to cart.\n")

    print_bill(items)


if __name__ == "__main__":
    main()
