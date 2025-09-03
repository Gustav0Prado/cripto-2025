import random, time

UTF8_MAX: int = 11263

def substitute_enc(text:str) -> str:
    out = ""
    for char in text:
        randint = random.randrange(0, UTF8_MAX)
        out += chr( ord(char) + randint )

    return out

def substitute_dec(text: str) -> str:
    out = ""
    
    for char in text:
        randint = random.randrange(0, UTF8_MAX)
        out += chr(abs(ord(char) -  randint))

    return out


def encrypt(input: str, output: str, key: str) -> float:
    time_exec = time.perf_counter()
    
    random.seed(key)

    with open(input, 'r') as input_file:
        with open(output, 'w') as output_file:
            for line in input_file:
                subs = substitute_enc(line)

                # Transposição aqui
                # ciphered = subs + transp
                ciphered = subs

                output_file.write(ciphered)

    return (time.perf_counter() - time_exec)

def decrypt(input: str, output: str, key: str) -> float:
    time_exec = time.perf_counter()
    
    random.seed(key)

    with open(input, 'r') as input_file:
        with open(output, 'w') as output_file:
            for line in input_file:
                subs = substitute_dec(line)

                # Transposição aqui
                # ciphered = subs + transp
                ciphered = subs

                output_file.write(ciphered)

    return (time.perf_counter() - time_exec)