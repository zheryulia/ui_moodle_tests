"""
Генерация случайных недействительных значений полей.
"""

import random

from faker import Faker


fake = Faker("Ru-ru")


class UserDataConstants:

    EMAIL_DISPLAY_MODES = {
        "видят_никто": "0",
        "видят_все": "1",
        "видят_однокурсники": "2",
    }
    TIMEZONE_VALUES = (
        "абвгд",
        "123"
        "Азия/Красноярск",
        "Европа/Киев",
        "UTC",
    )


class UserData:
    def __init__(
        self,
        name=None,
        last_name=None,
        email=None,
        moodle_net_profile=None,
        email_display_mode=None,
        city=None,
        timezone=None,
        about=None
    ):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.moodle_net_profile = moodle_net_profile
        self.email_display_mode = email_display_mode
        self.city = city
        self.timezone = timezone
        self.about = about

    @staticmethod
    def random():
        name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        moodle_net_profile = fake.url()
        email_display_mode = random.choice(
            list(UserDataConstants.EMAIL_DISPLAY_MODES.values())
        )
        city = fake.city_name()
        timezone = random.choice(UserDataConstants.TIMEZONE_VALUES)
        about = fake.text(max_nb_chars=200)
        return UserData(
            name,
            last_name,
            email,
            moodle_net_profile,
            email_display_mode,
            city,
            timezone,
            about,
        )