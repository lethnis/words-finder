def filter_length(words: list, length: int) -> list:
    """Filters words by length.
    Args:
        words: list of words.
        length: desired length.
    Returns:
        list of words with specified length."""

    return [word for word in words if len(word) == int(length)]


def filter_exclude(words: list, letters: str) -> list:
    """Removes word from the list if it contains any prohibited letter.
    Args:
        words: list of words.
        letters: single string with letters.
    Returns:
        new list of words without words with prohibited letters."""

    result = []
    for word in words:
        if not any(letter in word for letter in letters):
            result.append(word)
    return result


def filter_include(words: list, letters: str) -> list:
    """Removes word from the list if it not contains all required letters.
    Args:
        words: list of words.
        letters: single string with letters.
    Returns:
        new list of words without words that does not contain all required letters."""

    result = []
    for word in words:
        if all(letter in word for letter in letters):
            result.append(word)
    return result


def filter_inplace(words: list, letters: str) -> list:
    """Removes word from the list if it not contains all certain letters at certain places.
    Args:
        words: list of words.
        letters: single string with letters.
    Returns:
        new list of words without words that does not contain all certain letters at certain places."""

    result = []
    pairs = _get_pairs(letters)

    for word in words:
        if all(pair[0] == word[int(pair[1]) - 1] for pair in pairs):
            result.append(word)

    return result


def filter_not_inplace(words: list, letters: str) -> list:
    """Removes word from the list if it contains all certain letters at places where it should not be.
    Args:
        words: list of words.
        letters: single string with letters.
    Returns:
        new list of words without words that does not contain all certain letters at places where it should not be."""

    result = []
    pairs = _get_pairs(letters)

    for word in words:
        if all(pair[0] != word[int(pair[1]) - 1] for pair in pairs):
            result.append(word)

    return result


def _get_pairs(letters: str) -> list:
    """Helper function for filter_inplace, filter_not_inplace functions.
    Args:
        letters: single string with letters and digits (like: a1d2r5)
    Returns:
        list with letters and digits divided into individual pairs."""

    pairs = []
    for i in range(0, len(letters), 2):
        pair = letters[i : i + 2]
        if len(pair) == 2:
            pairs.append(pair)
    return pairs
