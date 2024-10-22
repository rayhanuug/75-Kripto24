def shift_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def shift_decrypt(text, shift):
    return shift_encrypt(text, -shift)

plaintext = "Rayhan Nugrah Kristio"
shift_value = 3  
ciphertext = shift_encrypt(plaintext, shift_value)
decryptedtext = shift_decrypt(ciphertext, shift_value)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decryptedtext}")
