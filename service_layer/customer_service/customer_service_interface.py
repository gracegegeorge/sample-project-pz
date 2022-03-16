from abc import ABC, abstractmethod

from data_access_layer.customer_data_access.customer_dao_interface import CustomerDAOInterface
from entities.customer_class_info import Customer


class CustomerServiceInterface(ABC):

    def __init__(self, customer_dao: CustomerDAOInterface):
        self.customer_dao = customer_dao

    @abstractmethod
    def create_customers_table(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def delete_from_customers_table_by_id(self, customer_id: str) -> bool:
        pass
