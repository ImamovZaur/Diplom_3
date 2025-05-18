from faker import Faker


def generate_email():
    fake = Faker()
    email = fake.email()
    return email


def generate_password():
    fake = Faker()
    password = fake.password()
    return password


def generate_name():
    fake = Faker()
    name = fake.name()
    return name


def generate_users():
    payload = {
        "email": generate_email(),
        "password": generate_password(),
        "name": generate_name()
    }
    return payload