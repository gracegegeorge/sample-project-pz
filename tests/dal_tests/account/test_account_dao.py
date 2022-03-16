from custom_exceptions.no_account_found import NoAccountFound
from data_access_layer.account_dal.account_dao_imp import AccountDaoImp
from entities.account_class_info import Account

account_dao = AccountDaoImp()


def test_create_account_success():
    account = Account(0, -2, 500.00)
    result = account_dao.create_account_record(account)
    assert result.account_id != 0


def test_create_account_non_int_id():
    account = Account("Zero", -2, 500.00)
    result = account_dao.create_account_record(account)
    assert result.account_id != 0


def test_select_account_by_id_success():
    result = account_dao.select_account_by_id(-2)
    assert result.account_id == -2


def test_no_account_found_by_id():
    try:
        account_dao.select_account_by_id(0)
        assert False
    except NoAccountFound as e:
        assert str(e) == "No account found with given id"


def test_select_all_accounts_by_customer_id_success():
    accounts = account_dao.select_all_accounts_by_customer_id(-2)
    assert len(accounts) >= 2


def test_select_all_accounts_by_customer_id_no_accounts():
    try:
        account_dao.select_all_accounts_by_customer_id(-1000)
        assert False
    except NoAccountFound as e:
        assert str(e) == "No accounts found with given id"


def test_update_account_by_id_success():
    account = Account(-3, -2, 600.00)
    result = account_dao.update_account_by_id(account)
    assert result.balance == 600.00


def test_update_account_no_records_changed():
    try:
        account_dao.select_all_accounts_by_customer_id(-1000)
        assert False
    except NoAccountFound as e:
        assert str(e) == "No accounts found with given id"


def test_transfer_success():
    result = account_dao.transfer_funds(-5, -6, 100.00)
    assert result


def test_transfer_sender_account_not_found():
    try:
        account_dao.transfer_funds(-1000, -6, 100.00)
        assert False
    except NoAccountFound as e:
        assert str(e) == "Sender account not found with given id"


def test_transfer_receiver_account_not_found():
    try:
        account_dao.transfer_funds(-5, -6000, 100.00)
        assert False
    except NoAccountFound as e:
        assert str(e) == "Receiver account not found with given id"


def test_delete_account_by_id_success():
    result = account_dao.delete_account_by_id(-4)
    assert result


def test_nothing_deleted_by_delete_method():
    try:
        account_dao.delete_account_by_id(-1000)
        assert False
    except NoAccountFound as e:
        assert str(e) == "No account found with given id"
