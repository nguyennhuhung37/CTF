def complex_xor_shuffle_encrypt(plaintext, key, output_file):
    key_len = len(key)
    encrypted = [
        chr(ord(char) ^ ord(key[i % key_len]))
        for i, char in enumerate(plaintext)
    ]
    ciphertext = ''.join(encrypted[::-1])
    
    with open(output_file, "w") as f:
        f.write(ciphertext)
    print(f"Ciphertext has been written to {output_file}")

flag = "CTB{fake_flag}"
key = "./key.txt"
output_file = "encrypted_flag.txt"

complex_xor_shuffle_encrypt(flag, key, output_file)
