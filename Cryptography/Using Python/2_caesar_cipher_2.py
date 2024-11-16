alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def conatians_only_alphabets(input_str):
    for char in input_str:
        if not char.isalpha():
            return False
        return True

while True:
    try:
        msg = input("Enter your message:")

        if conatians_only_alphabets(msg):
            break
        else:
            print("Input message does not contain alphabets only")
    except ValueError:
        print("Input is not an alphabet")

while True:
    try:
        key= int(input("Enter a num betweeen 1 - 26: "))
        if 1 <= key <= 26:
            break
        else:
            print("Input is not between 1 and 26.") 
    except ValueError:
        print("Input is not a number.")

def ceaser_encryption(text,shift):
    encrypted_text = ''
    #changing text to upper (or lower) case 
    text = text.upper()
    #length of text
    n = len(text)
    #encrypt text
    for i in range(n):
        c = text[i]
        loc = alpha.find(c)
        newloc = (loc + shift) % 26
        encrypted_text += alpha[newloc]
    return encrypted_text

def caesar_decryption(encrypted_text, shift):
    decypted_text = ''

        #length of encypted text
    n = len(encrypted_text)

        #decrypt text
    for i in range(n):
        c = encrypted_text[i]
        loc = alpha.find(c)
        newloc = (loc - shift) % 26
        decrypted_text += alpha[newloc]

    return decrypted_text

ciphertext = ceaser_encryption(msg, key)
decrypted_text = caesar_decryption(ciphertext, key)
print("Plaintext: ", msg)
print("Shift key: ", key)
print("Ciphertext: ", ciphertext)
print("Decrypted text: ", decrypted_text)