from data_access_layer.customer_data_access.customer_dao_interface import CustomerDAOInterface
from entities.customer_class_info import Customer


class CustomerDAOImp(CustomerDAOInterface):



    def insert_into_customers_table(self, customer_obj: Customer) -> Customer:
        # set up sql
        #create cursor
        # use cursor to execute sql transaction
        #remember to commit transaction
        #get th ereturned generated id
        # assign it to my customer obj
        # return customer obj

        sql = "Insert into customers values(default, %s, %s returning customer_id"
        cursor = connection.cursor()
        cursor.execute(sql, (customer_obj.first_name, customer_obj.last_name))
        connection.commit()
        returned_id = cursor.fetchone()[0]
        customer_obj.customer_id = returned_id
        return customer_obj



    def delete_from_customers_table_by_id(self, customer_id: int) -> bool:
        sql = "Delete from customers where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        if cursor.rocount != 0:
            return True
        else:
            return False



