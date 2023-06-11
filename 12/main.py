import hashlib
import time
from Crypto import Random
from Crypto.Util.number import getRandomRange
from Crypto.PublicKey import ElGamal, RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import ecdsa

# Генерация ключевой пары RSA
key = RSA.generate(2048)

# Подписание сообщения RSA
message = b"hdkjflshkjkw'sdfls"
start_time = time.time()
hash_obj = SHA256.new(message)
signature = PKCS1_v1_5.new(key).sign(hash_obj)
end_time = time.time()
print(f"Время подписи сообщения RSA: {end_time - start_time} секунд")

# Проверка подписи RSA
try:
    PKCS1_v1_5.new(key.publickey()).verify(hash_obj, signature)
    print("Подпись действительна.")
except (ValueError, TypeError):
    print("Подпись недействительна.")

# Генерация ключевой пары Шнорра
sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

# Подписание сообщения Шнорра
start_time = time.time()
hash_obj = hashlib.sha256(message).digest()
signature = sk.sign(hash_obj, sigencode=ecdsa.util.sigencode_der)
end_time = time.time()
print(f"Время подписи сообщения Шнорра: {end_time - start_time} секунд")

# Проверка подписи Шнорра
vk = sk.get_verifying_key()
if vk.verify(signature, hash_obj, sigdecode=ecdsa.util.sigdecode_der):
    print("Подпись действительна.")
else:
    print("Подпись недействительна.")

# Генерация ключевой пары Эль-Гамаля
ke = ElGamal.generate(2048, Random.get_random_bytes)

# Подписание сообщения Эль-Гамаля
start_time = time.time()
hash_obj = SHA256.new(message)
k = getRandomRange(1, ke.q)
signature = ke.sign(hash_obj, k)
end_time = time.time()
print(f"Время подписи сообщения Эль-Гамаля: {end_time - start_time} секунд")

# Проверка подписи Эль-Гамаля
if ke.verify(hash_obj, signature):
    print("Подпись действительна.")
else:
    print("Подпись недействительна.")
