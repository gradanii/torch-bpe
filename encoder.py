from functions import key_by_value

def og_bpe(string):
    # Step 1: Pairing all the letters and creating a list of all pairs
    pairs = []

    for i in range(0, len(string)):
        sub = string[i:i+2]
        if len(sub) == 2:
            pairs.append(sub)

    # Step 2: Find frequencies of pairs
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

    # Step 3: Assign single bytes to pairs
    new_bytes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

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


    

    
og_bpe('aaabcaaabac')