#!/usr/bin/python3

import random, sys

UTF8_MAX: int = 11263

def encrypt(input: str, output: str, key: str) -> None:
    random.seed(key)

    with open(output, 'w') as output_file:
        with open(input, 'r') as input_file:
            for line in input_file:
                for char in line:
                    randint = random.randrange(0, UTF8_MAX)
                    output_file.write( chr( ord(char) +  randint) )

def decrypt(input: str, output: str, key: str) -> None:
    random.seed(key)

    with open(output, 'w') as output_file:
        with open(input, 'r') as input_file:
            for line in input_file:
                for char in line:
                    randint = random.randrange(0, UTF8_MAX)
                    output_file.write( chr( abs(ord(char) -  randint)) )

encrypt(sys.argv[1], "enc.txt", "chave")
decrypt("enc.txt", "dec.txt", "chavelegal")