class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        try:
            with open(self.__file_name, 'r') as file:
                existing_products = file.read().strip().split('\n')
        except FileNotFoundError:
            existing_products = []

        with open(self.__file_name, 'a') as file:
            for product in products:
                product_str = str(product)
                if product_str in existing_products:
                    print(f"Продукт {product.name} уже есть в магазине")
                else:
                    file.write(product_str + '\n')
                    existing_products.append(product_str)


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
