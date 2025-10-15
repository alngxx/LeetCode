def stringMatching(self, words: List[str]) -> List[str]:
    sub_strings = set()
    for i in words:
        for j in words:
            if i != j and i in j:
                sub_strings.add(i)

    return list(sub_strings)
