from abc import ABC, abstractmethod


class IDatabase(ABC):

    @abstractmethod
    def create_discount(self):
        '''Interface method to create a discount.'''

    @abstractmethod
    def read_discount(self):
        '''Interface method to read a discount.'''

    @abstractmethod
    def update_discount(self):
        '''Interface method to update a discount.'''

    @abstractmethod
    def delete_discount(self):
        '''Interface method to delete a discount.'''
