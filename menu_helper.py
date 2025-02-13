from utils import *

def run_menu():
    while True:
        print_menu()
        option = int(input("Option: "))
        match option:
            case 1:
                print_clients()
            case 2:
                create_client()
            case 3:
                print_products()
            case 4:
                create_product()
            case 5:
                make_payment()
            case 6:
                print_payments()
            case 10:
                break

def print_menu():
    print("Select an option:\n")
    print("\t1. See Clients")
    print("\t2. Create a new Client")
    print("\t3. See Products")
    print("\t4. Create a product")
    print("\t5. Make a payment")
    print("\t6. See all Payments")
    print("\t10. Exit\n\n")

def print_clients():
    clients = get_customers()

    if len(clients) > 0:
        print("\n---------> Clients <---------\n")
        count = 1
        for client in clients:
            print(f"{count}. {client['name']} - {client['email']}")
            count += 1
        print("\n---------> END Clients <---------\n")
    else:
        print("\nNo clients found!")
        print("Creating a new one...\n")
        create_client()

def print_payment_methods(client_id):
    methods = get_payment_methods(client_id)
    print("\n---------> Payment Methods <---------\n")
    count = 1
    for method in methods:
        print(f"{count}. {method['id']} - {method['card']['brand']} - {method['card']['last4']}")
        count += 1
    print("\n---------> END Payment Methods <---------\n")

def print_products():
    products = get_products()
    if len(products) > 0:
        print("\n---------> Products <---------\n")
        count = 1
        for product in products:
            price_id = product["default_price"]
            price = get_price(price_id)
            print(f"{count}. {product['name']} ({price.unit_amount / 100} {price.currency})")
            count += 1
        print("\n---------> END Products <---------\n")
    else:
        print("\nNo products found!")
        print("Creating a new one...\n")
        create_product()

def create_client():
    print("\nCreating client...\n")
    name = input("Name: ")
    email = input("Email: ")
    client_id = create_customer(name, email)
    if client_id is not None:
        print(f"\nUser created with id: {client_id}\n")
        return client_id
    else:
        print("Error creating user")
        return None

def create_product():
    print("\nCreating product...\n")
    name = input("Name: ")
    amount = int(input("Price amount: ")) * 100
    currency = input("Price currency: ")

    product_id = create_product_with_price(name, amount, currency)
    if product_id is not None:
        print("Product created!\n")
        return product_id
    else:
        print("Product not created!\n")
        return None


def make_payment():
    print("\n Select a client:")
    print_clients()
    
    client_index = input("Client number: ")
    client_id = get_customers()[int(client_index) - 1]["id"]
    methods = get_payment_methods(client_id)

    if len(methods) == 0:
        print("\nCreating a new payment method...")
        payment_id = create_payment_method()
        if payment_id is not None:
            print(f"Payment method created with id: {payment_id}")
            if link_payment_method(client_id, payment_id):
                print("Payment method linked to user")
            else:
                print("Payment method not linked")
        else:
            print("Payment method not created")
    else:
        print("\n Select a payment method:")
        print_payment_methods(client_id)
        payment_index = input("Payment number: ")
        payment_id = get_payment_methods(client_id)[int(payment_index) - 1]["id"]

    print("\n Select a product:")
    print_products()
    product_index = input("Product number: ")
    
    product = get_products()[int(product_index) - 1]
    product_id = product["id"]
    price_id = product["default_price"]
    price = get_price(price_id)

    if create_payment(client_id, price.unit_amount, price.currency, payment_id, product_id):
        print("\nPayment created!\n")
    else:
        print("\nError creating payment\n")

def print_payments():
    payments = get_all_payments()

    print("\n---------> Payments <---------\n")
    count = 1
    for payment in payments:
        amount = payment["amount"] / 100
        currency = payment['currency']
        status = payment['status']
        customer_id = payment['customer']
        customer = get_customer_by_id(customer_id)["name"]
        print(f"{count}. {customer} - {amount} {currency} - {status}")
        count += 1
    print("\n---------> END Payments <---------\n")