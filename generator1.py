import random


def KSI_generator():
    for _ in range(10):
        sweet = random.randint(1, 100)
        sour = random.randint(1, 100-sweet)
        salty = 100-sweet-sour
        yield {'sweet': sweet, 'sour': sour, 'salty': salty}


ksi_generator = KSI_generator()

for tastes in ksi_generator:
    print(tastes)
