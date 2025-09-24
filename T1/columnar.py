import time

########################### ENCRYPT ###########################
########################## FUNCTIONS ##########################


def create_matrix(text: str, key: str) -> list[list[str]]:
    key_len = len(key)

    remainder = len(text) % key_len
    if remainder != 0:
       text += " " * (key_len - remainder)

    return [list(text[i:i + key_len]) for i in range(0, len(text), key_len)]

def rebuild_ciphered_text(matrix: list[list[str]], key: str) -> str:
    order = [i for i, _ in sorted(enumerate(key), key=lambda x: x[1])]

    return "".join(matrix[row][col] for col in order for row in range(len(matrix)))

def encrypt(input: str, first_key: str, second_key: str) -> float:
    time_exec = time.perf_counter()
    with open('intermed.txt', 'w') as output_file, open(input, 'r') as input_file:
        text = input_file.read()

        transpose_text = rebuild_ciphered_text(create_matrix(text, first_key), first_key)
        ciphered_text = rebuild_ciphered_text(create_matrix(transpose_text, second_key), second_key)

        output_file.write(ciphered_text)

    return time.perf_counter() - time_exec

########################### DECRYPT ###########################
########################## FUNCTIONS ##########################

def reorder_matrix(matrix: list[list[str]], sl: list[tuple[int, str]], key_len: int) -> list[list[str]]:
    index_map = {orig_idx: idx for idx, (orig_idx, _) in enumerate(sl)}
    return [matrix[index_map[i]] for i in range(key_len)]

def create_transpose_matrix(text: str, key: str) -> list[list[str]]:
    key_len = len(key)

    remainder = len(text) % key_len
    if remainder != 0:
        text += " " * (key_len - remainder)

    columns = len(text) // key_len
    matrix = [list(text[i:i + columns]) for i in range(0, len(text), columns)]

    sl = sorted(enumerate(key), key=lambda x: x[1])
    reordered_matrix = reorder_matrix(matrix, sl, key_len)

    return [list(row) for row in zip(*reordered_matrix)]

def rebuild_deciphered_text(matrix: list[list[str]], key: str ) -> str:
    return "".join(ch for row in matrix for ch in row).rstrip()

def decrypt(output: str, second_key: str, first_key: str) -> float:
    time_exec = time.perf_counter()
    with open(output, 'w') as output_file, open('intermed.txt', 'r') as input_file:
            text = input_file.read()
            
            transpose_text = rebuild_deciphered_text(create_transpose_matrix(text, first_key), first_key)
            deciphered_text = rebuild_deciphered_text(create_transpose_matrix(transpose_text, second_key), second_key)

            output_file.write(deciphered_text)
    return time.perf_counter() - time_exec
