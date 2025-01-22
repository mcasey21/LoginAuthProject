def encrypt_ceaser(text):

    OrigCypher = {
    '5': 1, '7': 2, 'N': 3, 'o': 4, 'x': 5, 'C': 6, '$': 7,
    'H': 8, '@': 9, '8': 10, 'R': 11, 'X': 12, '"': 13, 'c': 14,
    'D': 15, '£': 16, 'q': 17, 'g': 18, 'P': 19, '^': 20, '6': 21,
    ':': 22, '#': 23, '_': 24, '4': 25, '%': 26, 'v': 27, 's': 28,
    '(': 29, 'd': 30, '?': 31, ',': 32, '1': 33, 'r': 34, 'w': 35,
    ']': 36, '+': 37, 'L': 38, ')': 39, 'z': 40, 'u': 41, 'Q': 42,
    '9': 43, 'b': 44, '=': 45, 'k': 46, 'O': 47, 'h': 48, 'f': 49,
    'U': 50, '[': 51, '~': 52, '2': 53, '}': 54, 'a': 55, "'": 56,
    'e': 57, 'Y': 58, '.': 59, 'J': 60, '>': 61, 'Z': 62, 'M': 63,
    '{': 64, 'A': 65, 'i': 66, '&': 67, 'l': 68, '-': 69, 'K': 70,
    't': 71, 'n': 72, 'W': 73, '3': 74, '|': 75, 'T': 76, '\\': 77,
    '!': 78, '/': 79, 'm': 80, 'G': 81, 'I': 82, 'E': 83, '*': 84,
    ';': 85, 'V': 86, 'j': 87, 'B': 88, 'S': 89, 'p': 90, 'F': 91,
    '<': 92, 'y': 93
    }

    CC_key = 5

    def get_key_by_value(dictionary, value):
        for key, val in dictionary.items():
            if val == value:
                return key
        
    EncryptedCypher = {} # create new empty dict to allow encrypted values
    for key, value in OrigCypher.items():
        # wrap around and encryption logic
        # % 94 to keep it within the range of the cyper
        # copy new alphabet numbers into a new dict
        EncryptedCypher[key] = (value + CC_key - 1) % 93 + 1

    encrypted_message = ""

    for char in text:
        # encrypt if the character is in the alphabet
        if char in OrigCypher:
            # get the shifted value
            # find the letter using function
            encrypted_value = EncryptedCypher[char]
            encrypted_char = get_key_by_value(OrigCypher, encrypted_value)
            encrypted_message += encrypted_char
        else:
            # skip non-alphabet characters
            encrypted_message += char

    return encrypted_message
