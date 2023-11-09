def calculate_total_price(is_tuesday, num_pizzas, is_delivery, ordered_via_app):
    # Constants
    PIZZA_PRICE = 12
    DELIVERY_COST = 2.50
    APP_DISCOUNT = 0.25

    # Apply Tuesday Discount
    if is_tuesday:
        pizza_price = PIZZA_PRICE / 2
    else:
        pizza_price = PIZZA_PRICE

    # Calculate delivery cost
    if is_delivery and num_pizzas < 5:
        delivery_price = DELIVERY_COST
    else:
        delivery_price = 0

    # Calculate total price before app discount
    total_price = (pizza_price * num_pizzas) + delivery_price

    # Apply App Discount
    if ordered_via_app:
        total_price *= (1 - APP_DISCOUNT)

    return total_price


def main():
    print("Welcome to Beckett Pizza Plaza (BPP) Order Calculator")

    # Get user input
    is_tuesday = input("Is it Tuesday? (yes/no): ").strip().lower() == "yes"
    num_pizzas = int(input("Enter the number of pizzas in the order: "))
    is_delivery = input("Is this a delivery order? (yes/no): ").strip().lower() == "yes"
    ordered_via_app = input("Did the customer order via the BPP App? (yes/no): ").strip().lower() == "yes"

    # Calculate total price
    total_price = calculate_total_price(is_tuesday, num_pizzas, is_delivery, ordered_via_app)

    # Display the total price with 2 decimal places
    print(f"Total price: £{total_price:.2f}")

if __name__ == "__main":
    main()
