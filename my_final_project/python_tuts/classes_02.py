class Product:
    """Simple example class"""

    def __init__(self, product_code, product_name):
        self.product_code = product_code
        self.product_name = product_name

    def __repr__(self) -> str:
        return f"Product({self.product_code}, '{self.product_name}')"


class AldiProduct(Product):
    def __init__(self, product_code,product_name, aldi_code):
        super().__init__(product_code, product_name)
        self.aldi_code = aldi_code

    def __repr__(self) -> str:
        return f"Product({self.product_code}, '{self.product_name}', {self.aldi_code})"



p = AldiProduct(5825, 'BBQ Chops', 5555)
print(p)