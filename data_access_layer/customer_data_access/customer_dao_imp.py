from custom_exceptions.connection_problem import ConnectionProblem
from custom_exceptions.nothing_deleted import NothingDeleted
from data_access_layer.customer_data_access.customer_dao_interface import CustomerDAOInterface
from entities.customer_class_info import Customer
from utils.create_connection import connection


class CustomerDAOImp(CustomerDAOInterface):

    def create_customers_table(self, customer: Customer) -> Customer:
        # set up sql
        # create cursor
        # use cursor to execute sql transaction
        # remember to commit transaction
        # get th returned generated id
        # assign it to my customer obj
        # return customer obj
        try:
            sql = "INSERT INTO customers values (default, %s, %s) returning customer_id"
            cursor = connection.cursor()
            cursor.execute(sql, (customer.first_name, customer.last_name))
            connection.commit()
            returned_id = cursor.fetchone()[0]
            customer.customer_id = returned_id
            return customer
        except ConnectionProblem as e:
            raise ConnectionProblem(str(e))

    def delete_from_customers_table_by_id(self, customer_id: int) -> bool:
        try:
            sql = "delete from customers where customer_id =  %s"
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            if cursor.rowcount != 0:
                return True
            else:
                raise NothingDeleted("No record was deleted")
        except ConnectionProblem as e:
            raise ConnectionProblem(str(e))
