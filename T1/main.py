#!/usr/bin/python3

import argparse, aes, substitution, columnar, os
import pandas as pd
import matplotlib.pyplot as plt

parse = argparse.ArgumentParser(description="Argumentos para operação dos algoritmos")
parse.add_argument('-c', '--plain_text', type=str, help="Arquivo de Texto Claro")
parse.add_argument('-d', '--cypher_text', type=str, help="Arquivo de Texto Cifrado")
parse.add_argument('-a', '--aes', action='store_true', help="Usar AES para encriptação")
parse.add_argument('-o', '--output_file', type=str, help="Arquivo de Saída")
parse.add_argument('-s', '--substitution', action='store_true', help="Cifrar por substituição")
parse.add_argument('-t', '--transposition', action='store_true', help="Cifrar por transposição")
parse.add_argument('-b', '--benchmarking', action='store_true', help='Modelo para benchmarking')

args = parse.parse_args()


if args.benchmarking:
    def create_plot(df, title, filename):
        plt.figure(figsize=(12, 8))
        bars = plt.bar(df['Operation'], df['Time (seconds)'], color=['skyblue', 'lightcoral', 'lightgreen', 'orange'])
        plt.title(f'Encryption/Decryption Times - {title}', fontsize=14)
        plt.xlabel('Operation', fontsize=12)
        plt.ylabel('Time (seconds) - Log Scale', fontsize=12)
        plt.yscale('log')
        plt.xticks(rotation=45)
        
        for bar, value in zip(bars, df['Time (seconds)']):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), 
                    f'{value:.4f}', ha='center', va='bottom', fontsize=10)
        
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Gráfico salvo como: {filename}.png")

    files_list = ['./clear_text/1-LoremIpsum.txt', './clear_text/2-Frankenstein.txt', './clear_text/3-CompleteWorksShakespeare.txt']

    key: str = input("Insira sua chave: ")
    second_key: str = input("Insira sua segunda chave: ")
    times = [[],[],[]]
    i = 0
    for file in files_list:
        aes_encrypt_file = file+'.aes'
        aes_decrypt_file = file+'.aes.dec'
        students_encrypt_file = file+'.est'
        students_decrypt_file = file+'.est.dec'

        times[i].append(('AES - Enc', aes.encrypt(file, aes_encrypt_file, key)))
        times[i].append(('AES - Dec', aes.decrypt(aes_encrypt_file, aes_decrypt_file, key)))

        encrypt_time = columnar.encrypt(file, 'intermed.txt', key, second_key)
        encrypt_time += substitution.encrypt('intermed.txt', students_encrypt_file, key)
        times[i].append(('Students - Enc', encrypt_time))

        decrypt_time = substitution.decrypt(students_encrypt_file, 'intermed.txt',  key)
        decrypt_time += columnar.decrypt('intermed.txt', students_decrypt_file, key, second_key)
        times[i].append(('Students - Dec', decrypt_time))
        i += 1

    df1 = pd.DataFrame(times[0], columns=['Operation', 'Time (seconds)'])
    df1['File'] = files_list[0]

    df2 = pd.DataFrame(times[1], columns=['Operation', 'Time (seconds)'])
    df2['File'] = files_list[1]

    df3 = pd.DataFrame(times[2], columns=['Operation', 'Time (seconds)'])
    df3['File'] = files_list[2]

    create_plot(df1, "LoremIpsum", "10kb file")
    create_plot(df2, "Frankenstein", "500kb file")
    create_plot(df3, "Complete Works Shakespeare", "5mb file")

    print(times)
    os.remove('intermed.txt')
    exit(0)


if not args.output_file:
    raise ValueError("Insira um arquivo de saída para o programa")

if not args.plain_text and not args.cypher_text:
    raise ValueError("Insira um arquivo de texto claro (opção -c) ou um arquivo de texto criptografado (opção -d)")

if not args.aes and not args.substitution and not args.transposition:
    raise ValueError("Defina qual cifra usar com -a (AES) ou -s (Substituição) ou -t (Transposição Colunar)")

key: str = input("Insira sua chave: ")

time: float = 0.0
if args.plain_text:
    # Algoritmo AES
    if args.aes:
        time = aes.encrypt(args.plain_text, args.output_file, key)

    # Substituição + transposição
    if args.substitution and args.transposition:
        second_key: str = input("Insira sua segunda chave: ")
        time = columnar.encrypt(args.plain_text, "intermed.txt", key, second_key)
        time += substitution.encrypt("intermed.txt", args.output_file, key)
        os.remove("intermed.txt")

    # Só substituição
    elif args.substitution:
        time = substitution.encrypt(args.plain_text, args.output_file, key)

    # Só transposição
    elif args.transposition:
        second_key: str = input("Insira sua segunda chave: ")
        time = columnar.encrypt(args.plain_text, args.output_file, key, second_key)

elif args.cypher_text:
    # Algoritmo AES
    if args.aes:
        time = aes.decrypt(args.cypher_text, args.output_file, key)

    # Substituição + transposição
    if args.substitution and args.transposition:
        second_key: str = input("Insira sua segunda chave: ")
        time = substitution.decrypt(args.cypher_text, "intermed.txt", key)
        time += columnar.decrypt("intermed.txt", args.output_file, key, second_key)
        os.remove("intermed.txt")
    
    # Só substituição
    elif args.substitution:
        time = substitution.decrypt(args.cypher_text, args.output_file, key)
    
    # Só transposição
    elif args.transposition:
        second_key: str = input("Insira sua segunda chave: ")
        time = columnar.decrypt(args.cypher_text, args.output_file, key, second_key)

print(f'Tempo decorrido: {time:.5f}s')