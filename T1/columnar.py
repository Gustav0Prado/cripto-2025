import time

########################### ENCRYPT ###########################
########################## FUNCTIONS ##########################

def create_matrix(text: str, key: str) -> list[list[str]]:
    key_len = len(key)
    matrix = []

    remainder = (len(text) % key_len)
    if(remainder != 0):
        for i in range(remainder, key_len):
            text += ' '

    while text:
        line = []
        for i in range(key_len):
            line.append(text[0])
            text = text[1:]
        matrix.append(line)

    return matrix

def rebuild_ciphered_text(matrix: list[list[str]], key: str) -> str:
    sl = sorted(enumerate(key), key=lambda x: x[1])
    text = ''.join(
        str(matrix[i][sl[j][0]])
        for j in range(len(key))
        for i in range(len(matrix))
    )

    return text

def encrypt(input: str, output: str, first_key: str, second_key: str, third_key: str) -> float:
    time_exec = time.perf_counter()
    with open(output, 'w') as output_file:
        with open(input, 'r') as input_file:
            text = input_file.read()

            transposition_matrix = create_matrix(text, first_key)
            transpose_text = rebuild_ciphered_text(transposition_matrix, first_key)

            second_transpose = create_matrix(transpose_text, second_key)
            second_transpose_text = rebuild_ciphered_text(second_transpose, second_key)

            third_transpose = create_matrix(second_transpose_text, third_key)
            ciphered_text = rebuild_ciphered_text(third_transpose, third_key)

            output_file.write(ciphered_text)

    return time.perf_counter() - time_exec

########################### DECRYPT ###########################
########################## FUNCTIONS ##########################

def reorder_matrix(matrix: list[list[str]], sl: list[tuple[int, str]], key_len: int) -> list[list[str]]:
    ordered_matrix = []
    for i in range(key_len):
        index = next(idx for idx, (orig_idx, _) in enumerate(sl) if orig_idx == i)
        ordered_matrix.append(matrix[index])

    return ordered_matrix

def create_transpose_matrix(text: str, key: str) -> list[list[str]]:
    key_len = len(key)
    matrix = []
    remainder = (len(text) % key_len)
    if(remainder != 0):
        for i in range(remainder, key_len):
            text += ' '

    columns = (len(text) // key_len)
    while text:
        line = []
        for i in range(columns):
            line.append(text[0])
            text = text[1:]
        matrix.append(line)

    sl = sorted(enumerate(key), key=lambda x: x[1])
    reordered_matrix = reorder_matrix(matrix, sl, len(key))

    transposed_matrix = [list(row) for row in zip(*reordered_matrix)]
    return transposed_matrix

def rebuild_deciphered_text(matrix: list[list[str]], key: str ) -> str:
    text = ''.join(
        [str(matrix[i][j])
         for i in range(len(matrix))
         for j in range(len(matrix[i]))]
    ).rstrip()
    return text

def decrypt(input: str, output: str, third_key: str, second_key: str, first_key: str) -> float:
    time_exec = time.perf_counter()
    with open(output, 'w') as output_file:
        with open(input, 'r') as input_file:
            text = input_file.read()
            transposition_matrix = create_transpose_matrix(text, first_key)
            transpose_text = rebuild_deciphered_text(transposition_matrix, first_key)

            second_transpose = create_transpose_matrix(transpose_text, second_key)
            second_transpose_text = rebuild_deciphered_text(second_transpose, second_key)

            third_transpose = create_transpose_matrix(second_transpose_text, third_key)
            deciphered_text = rebuild_deciphered_text(third_transpose, third_key)

            output_file.write(deciphered_text)
    return time.perf_counter() - time_exec