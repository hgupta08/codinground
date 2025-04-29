def group_anagrams(words):
    anagrams = {}

    for word in words:
        sorted_word = ''.join(sorted(word))

        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    print(anagrams)

    return anagrams.values()


def main():
    input_string = "listen,stenli,cat,tac,act"
    words = input_string.split(',')
    grouped_anagrams = group_anagrams(words)
    print(grouped_anagrams)

    for group in grouped_anagrams:
        print(" ".join(group))


if __name__ == "__main__":
    main()