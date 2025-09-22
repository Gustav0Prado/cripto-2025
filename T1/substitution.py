import random, time

UTF8_MAX: int = 11263

def substitute(text:str) -> str:
    out = ""
    for char in text:
        randint = random.randrange(0, UTF8_MAX)
        out += chr( ord(char) ^ randint )

    return out

def encrypt(input: str, key: str) -> float:
    time_exec = time.perf_counter()
    
    random.seed(key)
    with open(input, 'r') as input_file:
        for line in input_file:
            subs = substitute(line)
                

    return (time.perf_counter() - time_exec), subs

def decrypt(input: str, output: str, key: str) -> float:
    time_exec = time.perf_counter()
    
    random.seed(key)

    with open(output, 'w') as output_file:
        for line in input:
            subs = substitute(line)
            output_file.write(subs)

    return (time.perf_counter() - time_exec)