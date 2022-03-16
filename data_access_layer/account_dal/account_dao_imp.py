from data_access_layer.account_dal.account_dao_interface import AccountDAOInterface
from entities.account_class_info import Account


class AccountDaoImp(AccountDAOInterface):

    def create_account_record(self, account: Account) -> Account:
        pass

    def select_account_by_id(self, account_id: int) -> Account:
        pass

    def select_all_accounts_by_customer_id(self, customer_id: int) -> list[Account]:
        pass

    def update_account_by_id(self, account: Account) -> Account:
        pass

    def transfer_account_by_id(self, sender_id: int, receiver_id: int, amount: float) -> bool:
        pass

    def delete_account_by_id(self, account_id: int) -> bool:
        pass
