#!/usr/bin/python3

import argparse
import aes

parse = argparse.ArgumentParser(description="Argumentos para operação dos algoritmos")

parse.add_argument('-c', '--plain_text', type=str, help="Arquivo de Texto Claro")
parse.add_argument('-d', '--cypher_text', type=str, help="Arquivo de Texto Cifrado")
parse.add_argument('-a', '--aes', action='store_true', help="Usar AES para encriptação")
parse.add_argument('-n', '--nova', action='store_true', help="Usar cifra Nova para encriptação")
parse.add_argument('-s', '--output_file', type=str, help="Arquivo de Saída", required=True)

args = parse.parse_args()

if not args.plain_text and not args.cypher_text:
    raise ValueError("Insira um arquivo de texto claro (opção -c) ou um arquivo de texto criptografado (opção -d)")

if not args.aes and not args.nova:
    raise ValueError("Defina qual cifra usar com -a (AES) ou -n (Nova)")

key = input("Insira sua chave: ")

time = 0
if args.plain_text:
    if args.aes:
        time = aes.encrypt_aes(args.plain_text, args.output_file, key)
    else:
        pass
elif args.cypher_text:
    if args.aes:
        time = aes.decrypt_aes(args.cypher_text, args.output_file, key)
    else:
        pass

print(f'Tempo decorrido: {time:.5f}s')