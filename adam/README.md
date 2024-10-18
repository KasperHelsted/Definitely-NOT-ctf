# Using OPENSSL to encrypt files

This is how we have encrypted the file given private key `adam` and public key `adam.pub`.

```
$ openssl genrsa -out adam 4096
$ openssl rsa -in adam -pubout -outform pem > adam.pub
$ openssl rand -base64 32 > key.bin
$ openssl enc -aes-256-ctr -salt -md sha512 -pbkdf2 -iter 100000 -in flag.txt -out flag.enc -pass file:./key.bin 
$ openssl pkeyutl -encrypt -inkey adam.pub -pubin -in key.bin -out key.enc 
```

You should be able to decrypt the code, if you have the full private key. Then by utilizing openssl as above (or using online tools):
1) Recover the private key
2) Decrypt the key.enc to recover the strong auto-generated password
3) Decrypt the flag.enc to recover the flag


This has been conducted using the following version: 
```
$ openssl version
OpenSSL 3.0.13 30 Jan 2024 (Library: OpenSSL 3.0.13 30 Jan 2024)
```