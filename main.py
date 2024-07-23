from src.mask import get_mask_card_number, get_mask_account
from src.utils import read_transactions


def main():
    print(get_mask_card_number("1234567890123456"))
    print(get_mask_account("12345678901234567890"))
    print(read_transactions("src/data/operations.json"))


if __name__ == '__main__':
    main()
