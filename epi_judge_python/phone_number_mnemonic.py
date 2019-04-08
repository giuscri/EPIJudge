from test_framework import generic_test, test_utils

KEYPAD = {
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
}

def phone_mnemonic(phone_number):
    if not phone_number:
        return [""]

    r = []
    suffixes = phone_mnemonic(phone_number[1:])
    for letter in KEYPAD.get(phone_number[0], phone_number[0]):
        for suffix in suffixes:
            r.append(letter + suffix)
    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
