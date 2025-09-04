#!/usr/bin/python3

import argparse, aes, new_cipher

parse = argparse.ArgumentParser(description="Argumentos para operação dos algoritmos")
parse.add_argument('-c', '--plain_text', type=str, help="Arquivo de Texto Claro")
parse.add_argument('-d', '--cypher_text', type=str, help="Arquivo de Texto Cifrado")
parse.add_argument('-a', '--aes', action='store_true', help="Usar AES para encriptação")
parse.add_argument('-n', '--new', action='store_true', help="Usar ? para encriptação")
parse.add_argument('-o', '--output_file', type=str, help="Arquivo de Saída", required=True)

args = parse.parse_args()

if not args.plain_text and not args.cypher_text:
    raise ValueError("Insira um arquivo de texto claro (opção -c) ou um arquivo de texto criptografado (opção -d)")

if not args.aes and not args.new:
    raise ValueError("Defina qual cifra usar com -a (AES) ou -n (??)")

key: str = input("Insira sua chave: ")

time: float = 0.0
if args.plain_text:
    if args.aes:
        time = aes.encrypt(args.plain_text, args.output_file, key)
    elif args.new:
        time = new_cipher.encrypt(args.plain_text, args.output_file, key)
elif args.cypher_text:
    if args.aes:
        time = aes.decrypt(args.cypher_text, args.output_file, key)
    elif args.new:
        time = new_cipher.encrypt(args.cypher_text, args.output_file, key)

print(f'Tempo decorrido: {time:.5f}s')