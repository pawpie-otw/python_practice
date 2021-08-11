import time
products = ["Product {}".format(i) for i in range(1, 500)]
promotions = ["Promotion {}".format(i) for i in range(1, 50)]
customers = ['Customer {}'.format(i) for i in range(1, 500)]


class Combinations:
    def __init__(self, products, promotions, customers) -> None:
        self.products = products
        self.promotions = promotions
        self.customers = customers
        self.current_product, self.current_promotion, self.current_customer = 0, 0, 0

    def __next__(self):
        if self.current_customer >= len(self.customers):
            self.current_customer = 0
            self.current_promotion += 1
        if self.current_promotion >= len(self.promotions):
            self.current_promotion = 0
            self.current_product += 1
        if self.current_product == len(self.products):
            raise StopIteration()
        item_to_return = f"""
{self.products[self.current_product]}\n
{self.customers[self.current_customer]}\n
{self.promotions[self.current_promotion]}\n
"""
        self.current_customer += 1
        return item_to_return

    def __iter__(self):
        return self


combinations = Combinations(products, promotions, customers)

for _ in combinations:
    pass

time.sleep(30)
