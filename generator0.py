def generator0():
    for product in range(1, 4):
        for promotion in range(1, 2):
            for customer in range(1, 5):
                yield (product, promotion, customer)
