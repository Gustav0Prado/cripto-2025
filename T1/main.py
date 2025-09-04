#!/usr/bin/python3

import argparse, aes, new_cipher, columnar

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
    raise ValueError("Defina qual cifra usar com -a (AES) ou -s (??) ou -t (Transposição Colunar)")

key: str = input("Insira sua chave: ")

time: float = 0.0
if args.plain_text:
    if args.aes:
        time = aes.encrypt(args.plain_text, args.output_file, key)
    elif args.substitution:
        time = new_cipher.encrypt(args.plain_text, args.output_file, key)
    elif args.transposition:
        second_key: str = input("Insira sua segunda chave: ")
        time = columnar.encrypt(args.plain_text, args.output_file, key, second_key)
elif args.cypher_text:
    if args.aes:
        time = aes.decrypt(args.cypher_text, args.output_file, key)
    elif args.substitution:
        time = new_cipher.encrypt(args.cypher_text, args.output_file, key)
    elif args.transposition:
        second_key: str = input("Insira sua segunda chave: ")
        time = columnar.decrypt(args.cypher_text, args.output_file, key, second_key)

print(f'Tempo decorrido: {time:.5f}s')