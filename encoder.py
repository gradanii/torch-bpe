from functions import key_by_value


def og_bpe(string):
    pairs = []

    for i in range(0, len(string)):
        sub = string[i : i + 2]
        if len(sub) == 2:
            pairs.append(sub)

    unique_pairs = sorted(list(set(pairs)))
    freq_pairs = []
    frequency = {}

    for i in unique_pairs:
        freq = pairs.count(i)
        frequency[i] = freq
        frequency = dict(sorted(frequency.items()))

    values = list(frequency.values())

    for i in values:
        if i > 1:
            pair = key_by_value(frequency, i)
            freq_pairs.append(pair)

    new_bytes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

    new_string = string

    for i in range(0, len(freq_pairs)):
        a = freq_pairs[i]
        b = new_bytes[i]
        new_string = new_string.replace(a, b)

    string = new_string
    freq_pairs.clear()

    if sum(list(frequency.values())) > len(frequency):
        og_bpe(new_string)
    else:
        print(new_string)


def mod_bpe(string):
    chars = list(dict.fromkeys(string))
    char_dict = {key: i for i, key in enumerate(chars)}
    char_list = list(string)

    while len(char_list) > 1:
        pairs = []

        for i in range(0, len(char_list)):
            pair = char_list[i : i + 2]
            if len(pair) == 2:
                pairs.append(pair)

        unique_pairs = sorted(pairs)
        frequency = {}

        for i in unique_pairs:
            freq = pairs.count(i)
            frequency["".join(i)] = freq

        frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

        max_val = max(char_dict.items(), key=lambda x: x[1])[1]

        most_freq_pair = list(frequency.keys())[0]

        char_dict[most_freq_pair] = max_val + 1

        print(char_dict)

        new_list = []
        i = 0

        while i < len(char_list):
            pair = "".join(char_list[i : i + 2])
            if pair == most_freq_pair:
                new_list.append(most_freq_pair)
                i += 2
            else:
                new_list.append(char_list[i])
                i += 1

        char_list = new_list

    print(char_list)


mod_bpe("apple")
