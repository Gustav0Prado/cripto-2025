#!/usr/bin/python3

import  aes, substitution, columnar


files_list = ['./clear_text/1-LoremIpsum.txt', './clear_text/2-Frankenstein.txt', './clear_text/3-CompleteWorksShakespeare.txt']


key: str = input("Insira sua chave: ")
second_key: str = input("Insira sua segunda chave: ")
aes_encrypt_time: float = []
aes_decrypt_time: float = []
students_encrypt_time: float = []
students_decrypt_time: float = []
tam = 10
for file in files_list:
    aes_encrypt_file = file+'.aes'
    aes_decrypt_file = file+'.aes.dec'
    students_encrypt_file = file+'.est'
    students_decrypt_file = file+'.est.dec'

    aes_encrypt_time.append(aes.encrypt(file, aes_encrypt_file, key))
    aes_decrypt_time.append(aes.decrypt(aes_encrypt_file, aes_decrypt_file, key))

    encrypt_time, intermed = substitution.encrypt(file, key)
    encrypt_time += columnar.encrypt(intermed, students_encrypt_file, key, second_key)
    students_encrypt_time.append((tam, encrypt_time))

    decrypt_time, intermed = columnar.decrypt(file, key, second_key)
    decrypt_time += substitution.decrypt(intermed, students_decrypt_file, key)
    students_decrypt_time.append((tam, decrypt_time))
    tam *= 10

print(f'Tempo decorrido: {aes_encrypt_time:.5f}s')
print(f'Tempo decorrido: {aes_decrypt_file:.5f}s')
print(f'Tempo decorrido: {students_encrypt_time:.5f}s')
print(f'Tempo decorrido: {students_decrypt_file:.5f}s')