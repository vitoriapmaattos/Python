import pytest

from Exercicio1 import Person, InvalidNameError, InvalidPhoneNumberError

def test_person_creation():
    person = Person("Willian Círico", "+55 47 9 9999-9999")

    assert person.name == "Willian Círico"
    assert person.phone == "+55 47 9 9999-9999"

def test_invalid_name():
    with pytest.raises(InvalidNameError):
        person = Person("Willian", "+55 47 9 9999-9999")

def test_invalid_phone():
    with pytest.raises(InvalidPhoneNumberError):
        person = Person("Willian Círico", "+55 47 9 99-9999")