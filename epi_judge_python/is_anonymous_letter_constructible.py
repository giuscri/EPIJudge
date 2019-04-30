from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    characters_available_in_magazine = dict()
    for character in magazine_text:
        characters_available_in_magazine[character] = characters_available_in_magazine.get(character, 0) + 1

    for character in letter_text:
        characters_available_in_magazine[character] = characters_available_in_magazine.get(character, 0) - 1
        if characters_available_in_magazine[character] < 0:
            return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
