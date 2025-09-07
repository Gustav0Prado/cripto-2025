#!/usr/bin/python3

import argparse, aes, substitution, columnar, os

parse = argparse.ArgumentParser(description="Argumentos para operação dos algoritmos")
parse.add_argument('-c', '--plain_text', type=str, help="Arquivo de Texto Claro")
parse.add_argument('-d', '--cypher_text', type=str, help="Arquivo de Texto Cifrado")
parse.add_argument('-a', '--aes', action='store_true', help="Usar AES para encriptação")
parse.add_argument('-o', '--output_file', type=str, help="Arquivo de Saída", required=True)
parse.add_argument('-s', '--substitution', action='store_true', help="Cifrar por substituição")
parse.add_argument('-t', '--transposition', action='store_true', help="Cifrar por transposição")

args = parse.parse_args()

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
        third_key: str = input("Insira sua terceira chave: ")
        time = substitution.encrypt(args.plain_text, "intermed.txt", key)
        time += columnar.encrypt("intermed.txt", args.output_file, key, second_key, third_key)
        os.remove("intermed.txt")

    # Só substituição
    elif args.substitution:
        time = substitution.encrypt(args.plain_text, args.output_file, key)

    # Só transposição
    elif args.transposition:
        second_key: str = input("Insira sua segunda chave: ")
        third_key: str = input("Insira sua terceira chave: ")
        time = columnar.encrypt(args.plain_text, args.output_file, key, second_key, third_key)

elif args.cypher_text:
    # Algoritmo AES
    if args.aes:
        time = aes.decrypt(args.cypher_text, args.output_file, key)

    # Substituição + transposição
    if args.substitution and args.transposition:
        second_key: str = input("Insira sua segunda chave: ")
        third_key: str = input("Insira sua terceira chave: ")
        time = columnar.decrypt(args.cypher_text, "intermed.txt", key, second_key, third_key)
        time += substitution.decrypt("intermed.txt", args.output_file, key)
        os.remove("intermed.txt")
    
    # Só substituição
    elif args.substitution:
        time = substitution.decrypt(args.cypher_text, args.output_file, key)
    
    # Só transposição
    elif args.transposition:
        second_key: str = input("Insira sua segunda chave: ")
        third_key: str = input("Insira sua terceira chave: ")
        time = columnar.decrypt(args.cypher_text, args.output_file, key, second_key, third_key)

print(f'Tempo decorrido: {time:.5f}s')