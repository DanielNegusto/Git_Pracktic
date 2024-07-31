from src.utils import read_transactions
from src.widget import mask_account_card
import pprint


def main() -> None:
    transactions = read_transactions('data/transactions.csv')
    pprint.pprint(transactions[0:3])
    print(mask_account_card(transactions[2]["from"]))


if __name__ == "__main__":
    main()
