import unittest
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Util.Padding import pad, unpad
import urllib3
import json
import sys
import base64
import requests


class TestStringMethods(unittest.TestCase):

    def test_encryption(self):
        messages = [
            {
                "foo": "bar",
                "hello": "hello",
                "random": "random",
            },
            {
                "biraj": "adhikari",
                "sagar": "paudell",
                "aarush": "timalsina",
            },
            {
                "dhum": "tana",
                "tadham": "tananana",
                "tena": "tena",
            },

        ]
        for message in messages:
            response = self.send_message(json.dumps(message))
            response_dict = json.loads(response.json())
            for x in message.keys():
                self.assertEqual(message[x], response_dict[x])

        response = self.send_message(json.dumps(message))
        response_dict = json.loads(response.json())
        for x in message.keys():
            self.assertEqual(message[x], response_dict[x])

    def send_message(self, data):
        base_url = "http://127.0.0.1:8000"
        response = requests.get(f"{base_url}/getKey").json()
        server_public_key = response['public_key']

        key = b'Sixteen byte key'

        rsa_cipher = PKCS1_OAEP.new(RSA.import_key(server_public_key))
        encrypted_key = rsa_cipher.encrypt(key)

        cipher = AES.new(key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))

        request_data = {
            "message": str(base64.b64encode(ciphertext), 'utf-8'),
            "encrypted_key": str(base64.b64encode(encrypted_key), 'utf-8'),
            "initialization_vector": str(base64.b64encode(cipher.iv), 'utf-8'),
        }
        response = requests.post(f"{base_url}/message", json=request_data)
        return response
        # check that s.split fails when the separator is not a string


if __name__ == '__main__':
    unittest.main()
