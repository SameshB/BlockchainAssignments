## Assignment 1 (ClientServerSecureConnection)

Implementation of a client server model where the communication is secured using AES and RSA encryption. Here the message digest is
encrypted using AES encryption and the key used is encrypted using the public key provided by the server. By using assymetric encryption
(RSA) to provide a secure way to communicate the encryption key(AES), we can create a link where large amount data can be transmitted
in betweena client and server securely.

### Dependencies
- FastAPI
- Pycryptodome
- Jupyterlab or notebook

### Server
The following set of commands will start the server

``` 
python3 generatekeypair.py
uvicorn server:app --reload 
```

### Opening the notebook
<p> The client is implemented in a ipynb notebook. This file can be opened using jupyter lab/ notebook</p>

``` 
jupyter lab client.ipynb 
```
### Tests
You can directly run the main file inside the tests directory. 

## Assignment 2 (BitCoin Core installation and basic transactions on testnet)
Details inside the notebook
