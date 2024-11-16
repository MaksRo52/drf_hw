import stripe
from forex_python.converter import CurrencyRates
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def convert_rub_to_dollars(amount):
    """Перевод рубли в доллары"""
    c = CurrencyRates()
    rate = c.get_rate('RUB', "USD")
    return int(rate * amount)


def create_stripe_price(amount, product):
    """Создает цену в страйпе"""
    price = stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": product},
    )
    return price.get("id")


def create_stripe_product(product):
    """Создает продукт в страйпе"""
    products = product.course if product.course else product.lesson
    product_id = stripe.Product.create(name=products)
    return product_id.get("id")


def create_stripe_session(price):
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
