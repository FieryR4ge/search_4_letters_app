def search_4_vowels(phrase: str) -> set:
    """Searching vowels in a word"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search_4_letters(phrase: str, letters: str = 'aeiou') -> set:
    """returns set of letters from phrase"""
    return set(letters).intersection(set(phrase))
