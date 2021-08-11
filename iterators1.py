class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers
        self.__max_item = len(self.products) * \
            len(self.promotions)*len(self.customers)

    @property
    def max_item(self):
        return self.__max_item

    def __getitem__(self, item):
        if item >= self.max_item:
            raise StopIteration
        else:
            pos_products = item//(self.max_item//len(self.products))
            item %= len(self.promotions)*len(self.customers)
            pos_promotions = item//len(self.customers)
            item %= len(self.customers)
            pos_customers = int(item)
            print(pos_products, pos_promotions, pos_customers)
            return f"{self.products[pos_products]}, {self.promotions[pos_promotions]}, {self.customers[pos_customers]}"


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 6)]

combinations = Combinations(products, promotions, customers)

# for i in range(1, 31):
#     print(combinations[i])
iter_comb = iter(combinations)


next(iter_comb)
for c in iter_comb:
    print(c)
