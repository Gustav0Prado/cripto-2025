import time

def encrypt(input: str, output: str, key: str) -> float:
    time_exec: float = time.perf_counter()

    # Chave precisa ser > 0
    k_index: int = 0
    k_length: int = len(key)
    if len(key) <= 0:
        return (time.perf_counter() - time_exec)

    with open(output, '+w') as output_file:
        with open(input, 'r') as input_file:
            for line in input_file:
                for char in line:
                    # Novo char = char + chave[index]
                    new_char: str = chr(abs(ord(char) + ord(key[k_index])))
                    
                    # Repete chave até o tamanho do texto
                    k_index += 1
                    if k_index >= k_length:
                        k_index = 0

                    # Escreve na saida
                    output_file.write(new_char)
                

    time_exec = (time.perf_counter() - time_exec)
    return time_exec

def decrypt(input: str, output: str, key: str) -> float:
    time_exec: float = time.perf_counter()

    # Chave precisa ser > 0
    k_index: int = 0
    k_length: int = len(key)
    if len(key) <= 0:
        return (time.perf_counter() - time_exec)

    with open(output, '+w') as output_file:
        with open(input, 'r') as input_file:
            for line in input_file:
                for char in line:
                    # Novo char = char - chave[index]
                    new_char: str = chr(abs(ord(char) - ord(key[k_index])))

                    # Repete chave até o tamanho do texto
                    k_index += 1
                    if k_index >= k_length:
                        k_index = 0

                    # Escreve na saida
                    output_file.write(new_char)

    time_exec = (time.perf_counter() - time_exec)
    return time_exec