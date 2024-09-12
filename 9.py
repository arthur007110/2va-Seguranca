# a) Implementar uma função de geração de chaves RSA
def rsa_keygen(bits):
    p = next_prime(randint(2^(bits-1), 2^bits))
    q = next_prime(randint(2^(bits-1), 2^bits))
    
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    d = inverse_mod(e, phi_n)
    
    return (e, n), (d, n)

# b) Implementar uma função de criptografia RSA
def rsa_encrypt(message, public_key):
    e, n = public_key
    return power_mod(message, e, n)

# c) Implementar uma função de descriptografia RSA
def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    return power_mod(ciphertext, d, n)

# d) Testar as funções criadas
public_key, private_key = rsa_keygen(8)

message = 42

# Criptografar
ciphertext = rsa_encrypt(message, public_key)
print("Ciphertext:", ciphertext)

# Descriptografar
decrypted_message = rsa_decrypt(ciphertext, private_key)
print("Decrypted message:", decrypted_message)
