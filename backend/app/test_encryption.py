from app.services.encryption_service import (
    encrypt_value,
    decrypt_value
)

plain = "TEST_TOKEN_123"

encrypted = encrypt_value(plain)
decrypted = decrypt_value(encrypted)

print("PLAIN:", plain)
print("ENCRYPTED:", encrypted)
print("DECRYPTED:", decrypted)