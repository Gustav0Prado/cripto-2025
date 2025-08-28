import time

def encrypt(input: str, output: str, key: str) -> float:
    time_exec = time.time()

    with open(output, '+w') as output_file:
        with open(input, 'r') as input_file:
            line = input_file.readline().strip('\n')
            for char in line:
                output_file.write(char)

    time_exec = (time.time() - time_exec)
    return time_exec

def decrypt(input: str, output: str, key: str) -> float:
    time_exec = time.time()

    with open(output, '+w') as output_file:
        with open(input, 'r') as input_file:
            line = input_file.readline().strip('\n')
            for char in line:
                output_file.write(char)

    time_exec = (time.time() - time_exec)
    return time_exec