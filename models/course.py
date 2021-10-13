"""
Генерация случайных значений полей названия.
"""

from faker import Faker


fake = Faker("Ru-ru")


class NewCourse:
    def __init__(self, full_name=None, short_name=None):
        self.full_name = full_name
        self.short_name = short_name

    @classmethod
    def random(cls):
        full_name = fake.text(max_nb_chars=40)
        short_name = fake.text(max_nb_chars=20) + "YUL"
        return cls(full_name, short_name)
