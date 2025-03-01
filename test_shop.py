"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart(product):
    return Cart()


@pytest.fixture
def product1():
    return Product("Cheese", 115, "Just a cheese", 2)


@pytest.fixture
def product2():
    return Product("Bread", 70, "Just a bread", 1)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000) == True
        assert product.check_quantity(999) == True
        assert product.check_quantity(1001) == False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(100)
        assert product.quantity == 900

        # Проверяем покупку товара в количестве равном полной партии со склада
        product.buy(900)
        assert product.quantity == 0  # После покупки должно остаться 0

    def test_product_buy_more_than_available(self, product):
        try:
            product.buy(1200)
        except ValueError as e:
            assert str(e) == "Недостаточно товара на складе для покупки"

        # Проверяем, что количество не изменилось после неудачной попытки
        assert product.quantity == 1000


class TestCart:

    def test_cart_initialization(self, cart):
        assert cart.products == {}
        assert cart.get_total_price() == 0.0

    def test_add_product_to_cart(self, cart, product):
        cart.add_product(product, 2)
        assert product in cart.products
        assert cart.products[product] == 2

    def test_add_multiple_products(self, cart, product1, product2):
        cart.add_product(product1, 1)
        cart.add_product(product2, 3)
        assert product1 in cart.products
        assert product2 in cart.products
        assert cart.products[product1] == 1
        assert cart.products[product2] == 3

    def test_clear_cart(self, cart, product):
        cart.add_product(product, 5)
        cart.clear()
        assert len(cart.products) == 0

    def test_cart_total_price_with_multiple_products(self, cart, product1, product2):
        cart.add_product(product1, 1)
        cart.add_product(product2, 2)
        assert cart.get_total_price() == 115 + 140

    def test_buy_cart_not_enough_stock(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError) as excinfo:
            cart.buy()
        assert str(excinfo.value) == 'Недостаточно товара на складе для покупки'