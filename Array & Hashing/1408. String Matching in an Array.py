def stringMatching(self, words: List[str]) -> List[str]:
    sub_strings = set()  # Don't store the same string twice when adding
    for i in words:
        for j in words:
            if i != j and i in j:
                sub_strings.add(i)

    # Convert set -> list
    return list(sub_strings)
