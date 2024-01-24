import pytest

from Exercicio3 import PhoneBook 

from Exercicio1 import Person

def test_add_person ():
    phone_Book = PhoneBook("Agenda de Contatos.")

    phone_Book.add_person("Vitória Mattos", "+55 48 9 9866-4535")

    assert len(phone_Book.people) == 1
    assert phone_Book.people[0].name == "Vitória Mattos"

def test_add_person_failed(capfd): #capfd para testar mensagens do terminal
    """Testa se dará erro com a agenda lotada. Laço de repetição para criar varios contatos."""
    phone_Book = PhoneBook("Agenda de Contatos.")

    for i in range(10):
        phone_Book.add_person(f"Pessoa {i}", f"+55 48 9 9999-999{i}")

    phone_Book.add_person("Vitória Mattos", "+55 48 9 9866-4535")

    out, _ = capfd.readouterr()

    assert "Agenda Lotada." in out # compara a mensagem mostrada no terminal (out) com o assert
    assert len (phone_Book.people) == 10

    
def test_remove_person():
    phone_Book = PhoneBook("Agenda de Contatos.")

    phone_Book.add_person("Vitória Mattos", "+55 48 9 9866-4535")

    phone_Book.remove_person("Vitória Mattos")

    assert len(phone_Book.people) == 0

def test_remove_person_failed(capfd):
    phone_Book = PhoneBook("Agenda de Contatos.")

    phone_Book.add_person("Vitória Mattos", "+55 48 9 9866-4535")

    phone_Book.remove_person("Vitória")

    assert len(phone_Book.people) == 1

    out, _ = capfd.readouterr()

    assert "Pessoa não encontrada na agenda" in out # compara a mensagem mostrada no terminal (out) com o assert

def test_search_person(capfd):
    

