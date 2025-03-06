class Product:

    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return self.name

    def check_quantity(self, quantity) -> bool:

        return self.quantity >= quantity

    def buy(self, quantity):

        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError(f"Недостаточно {self} на складе для покупки")

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        if product in self.products:
            # Если продукт уже есть, увеличиваем количество
            self.products[product] += buy_count
        else:
            # Если продукта нет, добавляем его в словарь
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):

        if product in self.products:
            if remove_count is None or self.products[product] <= remove_count:
                del self.products[product]
            else:
                self.products[product] -= remove_count

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total = 0
        for product, count in self.products.items():
            total += product.price * count
        return total

    def buy(self):

        insufficient_products = []

        # Проверяем наличие всех продуктов в корзине
        for product, quantity in self.products.items():
            if not product.check_quantity(quantity):
                insufficient_products.append((product, quantity))

        # Если есть недостающие продукты, выбрасываем исключение
        if insufficient_products:
            # raise ValueError(f'Недостаточно товаров на складе для покупки: {insufficient_products}')
            products_list = ', '.join(
                f"{product} недостаточно: {quantity}" for product, quantity in insufficient_products)
            raise ValueError(f'Недостаточно товаров на складе для покупки: [{products_list}]')

        # Если все продукты есть, списываем количество
        for product, quantity in self.products.items():
            product.buy(quantity)

        # Очистка корзины после успешной покупки
        self.clear()

