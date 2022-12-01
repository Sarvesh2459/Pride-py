import binascii as B
import pride as P #importig pride.py file.


#taking key input from user
val1 = input("Enter your key: ") 
arr1 = bytes(val1, 'utf-8')

#taking plaintext input
val2 = input("Enter plaintext: ")
arr2 = bytes(val2, 'utf-8')


input_key = B.unhexlify(arr1)
input_plaintext = B.unhexlify(arr2)
object1 = P.Pride(input_key)
encrypted_text  = object1.encrypt(input_plaintext)
print("Encrypted text: ", P.b2s(B.hexlify(encrypted_text))) 
decrypted_text  = object1.decrypt(encrypted_text)
print("Decrypted text: ",P.b2s(B.hexlify(decrypted_text)))

