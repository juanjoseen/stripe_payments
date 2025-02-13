import os
import dotenv
import stripe
import stripe.error

dotenv.load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

def config_stripe():
    stripe.api_key = SECRET_KEY

def get_customers():
    try:
        customers = stripe.Customer.list()
        return customers["data"]
    except stripe.error.StripeError as error:
        print(f"Error getting users: {error.user_message}")
        return None

def get_customer_by_id(client_id: str):
    try:
        client = stripe.Customer.retrieve(client_id)
        return client
    except stripe.error.StripeError as error:
        print(f"Error getting user: {error.user_message}")
        return None

def create_customer(name: str, email: str) -> str:
    try:
        client = stripe.Customer.create(name=name, email=email)
        return client.id
    except stripe.error.StripeError as error:
        print(f"Error creating user: {error.user_message}")
        return None

def create_payment_method() -> str:
    try:
        method = stripe.PaymentMethod.create(type="card", card={"token": "tok_visa"})
        return method.id
    except stripe.error.StripeError as error:
        print(f"Error creating payment method: {error.user_message}")
        return None

def get_payment_methods(client_id: str):
    try:
        payment_methods = stripe.PaymentMethod.list(customer=client_id)
        return payment_methods["data"]
    except stripe.error.StripeError as error:
        print(f"Error getting payment methods: {error.user_message}")
        return None

def create_product_with_price(name: str, amount: int, currency: str):
    try:
        product = stripe.Product.create(name=name)
        price = stripe.Price.create(currency=currency, unit_amount=amount, product=product.id)
        stripe.Product.modify(product.id, default_price=price.id)
        return product.id
    except stripe.error.StripeError as error:
        print(f"Error creating product: {error.user_message}")
        return None

def link_payment_method(client_id: str, payment_id: str) -> bool:
    try:
        stripe.PaymentMethod.attach(payment_id, customer=client_id)
        return True
    except stripe.error.StripeError as error:
        print(f"Error linking payment method: {error.user_message}")
        return False

def get_products():
    try:
        products = stripe.Product.list()
        return products["data"]
    except stripe.error.StripeError as error:
        print(f"Error getting products: {error.user_message}")
        return None

def get_price(price_id: str):
    try:
        price = stripe.Price.retrieve(price_id)
        return price
    except stripe.error.StripeError as error:
        print(f"Error getting price: {error.user_message}")
        return None

def create_payment(customer: str, amount: int, currency: str, method: str, product_id: str) -> bool:
    try:
        stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            customer=customer,
            payment_method=method,
            confirm=True,
            automatic_payment_methods={"allow_redirects": "never", "enabled": True},
            metadata={"product_id": product_id}
        )
        return True
    except stripe.error.StripeError as error:
        print(f"Error creating payment: {error.user_message}")
        return False

def get_all_payments():
    try:
        payments = stripe.PaymentIntent.list()
        return payments["data"]
    except stripe.error.StripeError as error:
        print(f"Error getting payments: {error.user_message}")
        return None