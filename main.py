
from utils import *
from menu_helper import run_menu

if __name__ == '__main__':
    config_stripe()

    run_menu()

    # client_id = create_customer("Juan Elias", "juanjoseen@gmail.com")

    # if client_id is not None:
    #     print(f"User created with id: {client_id}")

    #     payment_id = create_payment_method()

    #     if payment_id is not None:
    #         print(f"Payment method created with id: {payment_id}")

    #         if link_payment_method(client_id, payment_id):
    #             print("Payment method linked to user")

    #             products = get_products()
    #             first = products[0]
                
    #             product_id = first["id"]
    #             name = first["name"]
    #             price_id = first["default_price"]
                
    #             print(f"Product({product_id}): {name}")

    #             price = get_price(price_id)

    #             if price is not None:
    #                 unit = price.unit_amount / 100
    #                 currency = price.currency
                    
    #                 print(f"Price: {unit} {currency}")

    #                 if create_payment(client_id, price.unit_amount, currency, payment_id):
    #                     print("Payment created")
    #                 else:
    #                     print("Error creating payment")
    #             else:
    #                 print("Price not found")
    #         else:
    #             print("Payment method not linked")
    #     else:
    #         print("Payment method not created")
    # else:
    #     print("User not created")