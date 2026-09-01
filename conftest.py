import pytest
from faker import Faker
@pytest.fixture
def correct_mail():  
    fake=Faker()
    correct_email=fake.email()
    return correct_email

@pytest.fixture
def incorrect_mail():  
    fake=Faker()
    incorrect_email=fake.name()
    return incorrect_email

@pytest.fixture
def password():  
    fake=Faker()
    password=fake.password()  
    return password

@pytest.fixture
def ad_name():
    fake=Faker()
    ad_name=fake.word()
    return ad_name

@pytest.fixture
def ad_description():
    fake=Faker()
    ad_description=fake.sentence()
    return ad_description

