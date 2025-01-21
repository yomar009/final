from faker import Faker
import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal

fake = Faker()

def create_fake_product():
    return {
        "name": fake.word(),
        "category": fake.word(),
        "price": round(fake.random_number(digits=3), 2),
        "availability": fake.boolean()
    }

id = factory.Sequence(lambda n: n)
name = FuzzyChoice(
    choices=[
        "Hat",
        "Pants",
        "Shirt",
        "Apple",
        "Banana",
        "Pots",
        "Towels",
        "Ford",
        "Chevy",
        "Hammer",
        "Wrench",
    ]
)
description = factory.Faker("text")
price = FuzzyDecimal(0.5, 2000.0, 2)
active = FuzzyChoice(choices=[True, False])
category = FuzzyChoice(
    choices=[
        "UNKNOWN",
        "CLOTHS",
        "FOOD",
        "HOUSEWARES",
        "AUTOMOTIVE",
        "TOOLS",
    ]
)