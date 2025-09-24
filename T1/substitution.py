import random, time

UTF8_MAX: int = 256

def substitute_bytes(data: bytes) -> bytes:
    out = bytearray()
    for b in data:
        randint = random.randrange(0, UTF8_MAX)
        out.append(b ^ randint)
    return bytes(out)

def encrypt(output: str, key: str) -> float:
    time_exec = time.perf_counter()
    random.seed(key)

    with open('intermed.txt', 'rb') as input_file, open(output, 'wb') as output_file:
        for chunk in iter(lambda: input_file.read(4096), b""):
            subs = substitute_bytes(chunk)
            output_file.write(subs)

    return (time.perf_counter() - time_exec)

def decrypt(input: str, key: str) -> float:
    time_exec = time.perf_counter()
    random.seed(key)

    with open(input, 'rb') as input_file, open('intermed.txt', 'wb') as output_file:
        for chunk in iter(lambda: input_file.read(4096), b""):
            subs = substitute_bytes(chunk)
            output_file.write(subs)

    return (time.perf_counter() - time_exec)