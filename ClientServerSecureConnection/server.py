from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Util.Padding import pad, unpad

from fastapi import FastAPI
from pydantic import BaseModel
import base64

from typing import Dict, Any


class Message(BaseModel):
    message: str
    encrypted_key: str
    initialization_vector: str


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/getKey")
def sendPublicKey():
    f = open('mykey.pem', 'r')
    key = RSA.import_key(f.read())
    public_key = key.public_key().export_key()
    return {"public_key": public_key}


@app.post("/message")
async def sendMessage(request_json: Message):

    message = base64.b64decode(request_json.message)
    encrypted_AES_key = base64.b64decode(request_json.encrypted_key)
    initialization_vector = base64.b64decode(
        request_json.initialization_vector)

    f = open('mykey.pem', 'r')
    private_key = RSA.import_key(f.read())
    cipher_rsa = PKCS1_OAEP.new(private_key)

    decrypt_key = cipher_rsa.decrypt(encrypted_AES_key)
    cipher = AES.new(
        decrypt_key,
        AES.MODE_CBC,
        iv=initialization_vector
    )
    original = unpad(cipher.decrypt(message), AES.block_size)
    print(original.decode())


    # return {}
    return original
