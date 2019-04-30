from test_framework import generic_test, test_utils


def find_anagrams(dictionary):
    anagrams = dict()
    for word in dictionary:
        #key = "".join(sorted(filter(lambda character: character != " ", word)))
        key = "".join(sorted("".join(word.split(" ")))) # way more efficient!
        value = anagrams.get(key, [])
        value.append(word)
        anagrams[key] = value

    r = []
    for k in anagrams.keys():
        if len(anagrams.get(k, [])) > 1:
            r.append(anagrams[k])
    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare))
