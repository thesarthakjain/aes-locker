<p align="center">
	<h1 align="center"> AES-LOCKER </h1>
	<h4 align="center"> Encrypt and decrypt any type of files using AES <h4>
</p>
<br>

## About the project:
- This script can be used to encrypt and decrypt any file using AES algorithm.
- The password entered by the user is converted to 256 bit key using SHA256 hashing algorithm.
- The key is then used to generate an initialization vector(IV) and encrypt/decrypt a file.
- The project uses this [cryptography library](https://github.com/pyca/cryptography).

## Pre-requisites:
- [X] Python 3.9.6+
- [X] Dependencies from requirements.txt

## Installing required python dependencies
- Clone this repository onto your system.
```
$ git clone https://github.com/thesarthakjain/aes-locker
```
- Then, install the packages from requirements.txt.
```
$ pip install -r requirements.txt
```

## Directions to run
- Put a file you wanna encrypt/decrypt in the project directory.
- Run the following command in the project directory:
```
$ python locker.py
```
