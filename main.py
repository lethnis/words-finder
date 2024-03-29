import streamlit as st

import filters as F


def main():
    """Main loop of the program. Creates a filter inputs and applies the to russian nouns"""

    # load all words into list
    words = open("russian_nouns.txt", encoding="utf-8").read().split("\n")

    # define two columns
    left, right = st.columns(2)

    # add different filters to the left column
    length = left.text_input("Введите длину слова:", placeholder="например: 5")
    include = left.text_input("Введите буквы, которые точно есть в слове:", placeholder="например: абвгд")
    exclude = left.text_input("Введите буквы, которых точно нет в слове:", placeholder="например: еёжзи")
    inplace = left.text_input(
        "Если известно точное положение буквы, введите в формате БукваМесто:",
        placeholder="например: а2а4 ('а' точно на 2 и 4 месте)",
    )
    not_inplace = left.text_input(
        "Если известно где буквы нет, но она точно есть в слове, введите в формате БукваМесто:",
        placeholder="например: б1 ('б' не на 1 месте)",
    )
    # add search button to the left column
    search = left.button("Поиск")

    # make a copy of all words
    found_words = words.copy()

    # when button pressed if there are any filters apply them
    if search:
        if length:
            found_words = F.filter_length(found_words, length)
        if include:
            found_words = F.filter_include(found_words, include)
        if exclude:
            found_words = F.filter_exclude(found_words, exclude)
        if inplace:
            found_words = F.filter_inplace(found_words, inplace)
        if not_inplace:
            found_words = F.filter_not_inplace(found_words, not_inplace)

    # add to the right side list of all found words
    right.text_area(label=f"Найдено слов {len(found_words)}", value="\n".join(found_words).strip(), height=400)


if __name__ == "__main__":
    main()
