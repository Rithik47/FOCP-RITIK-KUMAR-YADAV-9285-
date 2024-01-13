                                         #/////  BPP PIZZA PRICE CALCULATOR PROGRAM  ////

def get_order_details():
    while True:
        try:
            num_pizzas = int(input("How many pizzas ordered? "))
            if num_pizzas < 0:
                raise ValueError("Please enter a positive integer!")

            delivery_required = input("Is delivery required? (Y/N) ").upper()
            if delivery_required not in ['Y', 'N']:
                raise ValueError('Please answer "Y" or "N".')

            is_tuesday = input("Is it Tuesday? (Y/N) ").upper()
            if is_tuesday not in ['Y', 'N']:
                raise ValueError('Please answer "Y" or "N".')

            used_app = input("Did the customer use the app? (Y/N) ").upper()
            if used_app not in ['Y', 'N']:
                raise ValueError('Please answer "Y" or "N".')

            return num_pizzas, delivery_required, is_tuesday, used_app
        except ValueError as e:
            print(e)


def calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app):
    pizza_price = 12
    delivery_cost = 2.5
    app_discount = 0.25
    tuesday_discount = 0.5

    total_price = num_pizzas * pizza_price

    if is_tuesday == 'Y':
        total_price *= (1 - tuesday_discount)

    if delivery_required == 'Y':
        if num_pizzas >= 5:
            total_price += 0  # Free delivery
        else:
            total_price += delivery_cost

    if used_app == 'Y':
        total_price *= (1 - app_discount)

    return total_price


def main():
    print("BPP Pizza Price Calculator")
    print("==========================")

    num_pizzas, delivery_required, is_tuesday, used_app = get_order_details()

    total_price = calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app)

    print(f"\nTotal Price: £{total_price:.2f}.")


if __name__ == "__main__":
    main()
