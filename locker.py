import os
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import time

def clear():
    try:
        os.system('cls')
    except:
        os.system('clear')

def pad_file(file):
    while len(file)%16 != 0:
        file = file + b" "
    return file

def encrypt(key, iv, file_name):
    with open(file_name, 'rb') as f:
        orig_file = f.read()
        padded_file = pad_file(orig_file)
        f.close()


    enc_obj = Cipher(algorithms.AES(key), modes.CBC(iv)).encryptor()
    enc_text = enc_obj.update(padded_file) + enc_obj.finalize()

    with open(file_name + '.enc', 'wb') as f:
        f.write(enc_text)
        f.close()
    
    os.remove(file_name)

def decrypt(key, iv, file_name):
    with open(file_name, 'rb') as f:
        orig_file = f.read()
        f.close()

    dec_obj = Cipher(algorithms.AES(key), modes.CBC(iv)).decryptor()
    dec_text = dec_obj.update(orig_file) + dec_obj.finalize()

    with open(file_name[:-4], 'wb') as f:
        f.write(dec_text)
        f.close()
    
    os.remove(file_name)

def encryptor(password, file_name):
    clear()
    print('Encrypting:', file_name, " to ", file_name+".enc")
    key = hashlib.sha256(password).digest()
    iv = hashlib.sha256(password).digest()[:16]
    
    start_time = time.time()
    encrypt(key, iv, file_name)
    clear()
    print(file_name, "has been encrypted in", round((time.time() - start_time), 2), "seconds.")
    input("Press enter key to continue.")

def decryptor(password, file_name):
    clear()
    if file_name[-4:] != ".enc":
        file_name = file_name + '.enc'
        print('Decrypting:', file_name, " to ", file_name[:-4])
    else:
        print('Decrypting:', file_name, " to ", file_name[:-4])

    key = hashlib.sha256(password).digest()
    iv = hashlib.sha256(password).digest()[:16]
    
    start_time = time.time()
    decrypt(key, iv, file_name)
    clear()
    print(file_name, "has been decrypted in", round((time.time() - start_time), 2), "seconds.")
    input("Press enter key to continue.")

while(True):
    clear()
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = int(input("\nChoose any one option: "))
    clear()

    if choice == 1:
        file_name = input('Name of the file: ')
        clear()
        password = input('Enter password: ').encode()
        encryptor(password, file_name)
    elif choice == 2:
        file_name = input('Name of the file: ')
        clear()
        password = input('Enter password: ').encode()
        decryptor(password, file_name)
    elif choice == 3:
        exit()
    else:
        input("Choose another option.")