
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def encode():
    plain_text = str(input('Enter the text you would you like to encode: '))
    plain_text = plain_text.upper()
    # print(plain_text)

    shift_number = int(input('Enter the shift number: '))
    if shift_number >= 26 or shift_number <= 0:
        print('Shift number must be between 1 and 26')
        encode()

    coded_text = ''

    for i in range(0,len(plain_text)):
        if plain_text[i] in alphabet:
            for j in range (0, 26):
                if plain_text[i] == alphabet[j] and (j + shift_number) <= 26:
                    coded_text += alphabet[j + shift_number]
                elif plain_text[i] == alphabet[j] and (j + shift_number) > 26:
                    overflow = j + shift_number - 26
                    coded_text += alphabet[overflow]
        else:
            coded_text += plain_text[i]
    
    print(coded_text)


encode()