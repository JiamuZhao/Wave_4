def translator(w):
    vowel = ['a', 'e', 'i', 'o', 'u']
    if w[0] in vowel:
        return w + 'way'
    else:
        s = 0
        length = len(w)
        for i in range(0, length):
            if w[i] in vowel:
                s += 1
                break
        first_part = w[0:i]
        second_part = w[i:]
        return second_part + first_part + 'ay'
