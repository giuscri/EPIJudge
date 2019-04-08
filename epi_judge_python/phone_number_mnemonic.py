from test_framework import generic_test, test_utils

KEYPAD = {
    "0": "0",
    "1": "1",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
}

def helper_function(phone_number, idx, partial_mnemonic, mnemonics):
    if idx == len(phone_number):
        mnemonics.append("".join(partial_mnemonic))
        return

    for letter in KEYPAD[phone_number[idx]]:
        partial_mnemonic[idx] = letter
        helper_function(phone_number, idx + 1, partial_mnemonic, mnemonics)

def phone_mnemonic(phone_number):
    mnemonics = []
    partial_mnemonic = ["" for _ in phone_number]

    helper_function(phone_number, 0, partial_mnemonic, mnemonics)

    return mnemonics


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
