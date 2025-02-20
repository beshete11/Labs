class Caesar:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        plaintext = plaintext.lower()
        ciphertext = ""

        for char in plaintext:
            shift = ord(char) + self.key
            if shift > ord('z'):
                shift -= 26
            if shift < ord('a'):
                shift += 26

            ciphertext += chr(shift)

        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""

        for char in ciphertext:
            shift = ord(char) - self.key
            if shift < ord('a'):
                shift += 26
            if shift > ord('z'):
                shift -= 26
                
            plaintext += chr(shift)

        return plaintext



cipher = Caesar(-6)
print(cipher.encrypt("FFF"))
