# from collections.abc import Iterator
# from error_handl_decorator import error_handling_decorator
from Final_Project.error_handl_decorator import CustomError
from collections import UserDict
import re
import datetime
import pickle

from abc import ABC, abstractmethod

class UserInterface(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass
    
    @abstractmethod
    def display_notes(self, notes):
        pass
    
    @abstractmethod
    def display_commands(self, commands):
        pass
    
    @abstractmethod
    def get_user_input(self):
        pass

class ConsoleInterface(UserInterface):
    def display_contacts(self, contacts):
        print("Contacts:")
        for contact in contacts:
            print(contact)
    
    def display_notes(self, notes):
        print("Notes:")
        for note in notes:
            print(note)
    
    def display_commands(self, commands):
        print("Available Commands:")
        for command in commands:
            print(command)
    
    def get_user_input(self):
        return input("Enter your command: ")
    
class AddressBook(UserDict):
    def __init__(self, interface, file_name: str=None):
        self.__file_name = None
        self.file_name = file_name
        self.interface = interface
        super().__init__()
        self.restore()
    
    # ... (rest of the class remains the same)

    def show_contacts(self):
        self.interface.display_contacts(list(self.data.keys()))

    def show_notes(self):
        notes = [record.note.value for record in self.data.values() if record.note]
        self.interface.display_notes(notes)

    def show_commands(self, commands):
        self.interface.display_commands(commands)

    def get_user_input(self):
        return self.interface.get_user_input()
    
console_interface = ConsoleInterface()
phone_book = AddressBook(console_interface)