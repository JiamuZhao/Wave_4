def reverseLookup(a, b):
    keys_list = [key for key, value in a.items() if value == b]
    return keys_list
