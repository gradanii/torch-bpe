def key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None