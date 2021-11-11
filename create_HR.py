from cryptography.fernet import Fernet
from settings import CYPHER_KEY


phone = str(80000000000)
role = 'HR'
cipher = Fernet(CYPHER_KEY)
combined_data = phone + '...' + role
byte_text = str.encode(combined_data)
encrypted_bytekey = cipher.encrypt(byte_text) 
encrypted_key = encrypted_bytekey.decode()  # это  ключ доступа
print(
    'Вам сгенерирован ключ для доступа к HR функциям бота. '
    '\nЧтобы использовать ключ, скопируйте его, перейдите в бота инажмите кнопку "Войти по ключу", '
    '\nвставьте его в сообщение и отправьте боту.'
    '\n'
)
print(encrypted_key)