import time, string, random

###########################  SHARED  ##########################
########################## FUNCTIONS ##########################

def create_matrix(text: str, length: int) -> list[list[str]]:
    matrix = []
    remainder = (len(text) % length)
    if(remainder != 0):
        for i in range(remainder, length):
            text += random.choice(string.ascii_letters)
    while text:
        line = []
        for i in range(0,length):
            line.append(text[0])
            text = text[1:]
        matrix.append(line)
    return matrix

########################### ENCRYPT ###########################
########################## FUNCTIONS ##########################

def cipher_text(matrix: list[list[str]], key: str) -> str:
    sl = sorted(enumerate(key), key=lambda x: x[1])
    text = ""
    for j in range(0, len(key)):
        new_line = ""
        for i in range(0, len(matrix)):
            new_line += matrix[i][sl[j][0]]
        text += new_line

    return text

def encrypt(input: str, output: str, first_key: str, second_key: str) -> float:
    time_exec = time.perf_counter()
    first_len = len(first_key)
    second_len = len(second_key)
    with open(output, 'w') as output_file:
        with open(input, 'r') as input_file:
            text = input_file.read()

            transposition_matrix = create_matrix(text, first_len)
            transpose_text = cipher_text(transposition_matrix, first_key)

            second_transpose = create_matrix(transpose_text, second_len)
            ciphered_text = cipher_text(second_transpose, second_key)
            output_file.write(ciphered_text)

    return time.perf_counter() - time_exec;

########################### DECRYPT ###########################
########################## FUNCTIONS ##########################

def decipher_text(matrix: list[list[str]], key: str) -> str:
    sl = sorted(enumerate(key), key=lambda x: x[1])
    text = ""
    for j in range(0, len(key)):
        new_line = ""
        for i in range(0, len(matrix)):
            new_line += matrix[i][sl[j][0]]
        text += new_line

    return text

def decrypt(input: str, output: str, second_key: str, first_key: str) -> float: # NOT WORKING YET
    time_exec = time.perf_counter()
    first_len = len(first_key)
    second_len = len(second_key)
    with open(output, 'w') as output_file:
        with open(input, 'r') as input_file:
            text = input_file.read()
            transposition_matrix = create_matrix(text, first_len)
            transpose_text = decipher_text(transposition_matrix, first_key)

            second_transpose = create_matrix(transpose_text, second_len)
            deciphered_text = decipher_text(second_transpose, second_key)
            output_file.write(deciphered_text)
    return time.perf_counter() - time_exec;
