print("Hello, Contosoville")
town= "Contosoville"
print("The town I was looking for is " + town)

def chant(phrase):
    print(phrase+phrase+phrase)

chant(town)

def lasso_letter(letter, shiftamt):
    #ASCII code of letter saved in letter_code
    letter_code=ord(letter.lower())
    #ASCII Value of 'a'

    a_ascii = ord('a')
    alphabet_size=26

    #formula to calculate ASCII number for the decoded letter

    true_letter_code= a_ascii + (((letter_code-a_ascii)+ shiftamt) % alphabet_size)
    decoded_letter= chr(true_letter_code)
    return decoded_letter

#Single letter decoding
print(lasso_letter('p',-2))  

#List of letters - word decoding

def laso_word(word, shiftamt):
    decoded_word = ""
    for letter in word:
        decoded_letter=lasso_letter(letter, shiftamt)
        decoded_word = decoded_word + decoded_letter
    print(decoded_word)
laso_word('wjmmf', -1)

