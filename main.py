from src.utils import read_transactions, save_transactions
from src.widget import mask_account_card


def main() -> None:
    transactions = read_transactions('data/transactions.csv')
    print(mask_account_card(transactions[2]["from"]))


if __name__ == "__main__":
    main()
