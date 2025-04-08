class Product:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions  # (length, width, height)

    def __str__(self):
        return f"{self.name} - {self.price} грн ({self.description})"


class Customer:
    def __init__(self, last_name, first_name, middle_name, phone):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.phone = phone

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}, тел: {self.phone}"


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []  # список кортежів: (товар, кількість)

    def add_product(self, product, quantity):
        self.items.append((product, quantity))

    def total_price(self):
        return sum(product.price * quantity for product, quantity in self.items)

    def __str__(self):
        order_lines = [f"Замовлення для: {self.customer}\n"]
        for product, quantity in self.items:
            order_lines.append(f"{product.name} x{quantity} = {product.price * quantity} грн")
        order_lines.append(f"\nЗагальна сума: {self.total_price()} грн")
        return "\n".join(order_lines)


# --- Тестування ---
# Створюємо товари
product1 = Product("Ноутбук", 25000, "HP Pavilion 15", (36, 24, 2))
product2 = Product("Миша", 500, "Logitech USB", (10, 6, 4))

# Створюємо покупця
customer = Customer("Іваненко", "Іван", "Іванович", "+380671112233")

# Створюємо замовлення
order = Order(customer)
order.add_product(product1, 1)
order.add_product(product2, 2)

# Виводимо інформацію про замовлення
print(order)
