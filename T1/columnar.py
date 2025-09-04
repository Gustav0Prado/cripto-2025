import time

def encrypt(input: str, output: str, first_key: str, second_key: str) -> float:
    time_exec = time.perf_counter()
    # remove espacos do testo limpo
    # colocar o texto na matriz, o numero de linhas vai aumentar dinamicamente
    # o numero de colunas se da com base no comprimento da palavra
    return time.perf_counter() - time_exec;

def decrypt(input: str, output: str, first_key: str, second_key: str) -> float:
    time_exec = time.perf_counter()
    return time.perf_counter() - time_exec;
