from unittest.mock import patch

from custom_exceptions.connection_problem import ConnectionProblem
from custom_exceptions.nothing_deleted import NothingDeleted
from data_access_layer.customer_data_access.customer_dao_imp import CustomerDAOImp
from entities.customer_class_info import Customer

customer_dao = CustomerDAOImp()


def test_create_customer_record_success():
    test_customer = Customer(0, "Fabulous", "Bryan")
    returned_customer = customer_dao.insert_into_customers_table(test_customer)
    assert returned_customer.customer_id != 0


def test_delete_customer_record_success():
    result = customer_dao.delete_from_customers_table_by_id(1)
    assert result


@patch("utils.create_connection.create_connection")
def test_create_operational_error_caught(mock):
    try:
        mock.side_effect = ConnectionProblem("Could not connect to the database")
        customer_dao.create_customer_entry(Customer(0, "should not" "be added"))
        assert False
    except ConnectionProblem as e:
        assert str(e) == "Could not connect to the database"


@patch("utils.create_connection.create_connection")
def test_delete_customer_operational_error_caught(mock):
    try:
        mock.side_effect = ConnectionProblem("Could not connect to the database")
        customer_dao.delete_from_customers_table_by_id(0)
        assert False
    except ConnectionProblem as e:
        assert str(e) == "Could not connect to the database"


def test_delete_customer_no_records_changed():
    try:
        customer_dao.delete_from_customers_table_by_id(-1000)
        assert False
    except NothingDeleted as e:
        assert str(e) == "No record was deleted"
