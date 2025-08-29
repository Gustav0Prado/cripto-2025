import time

def to_ord(c: str) -> str:
    return str(f'{ord(c):04d}')

def to_char(c: str) -> str:
    return chr(int(c[0]+c[1]+c[2]+c[3]))

def encrypt(input: str, output: str, key: str) -> float:
    time_exec = time.time()

    with open(output, '+w') as output_file:
        with open(input, 'r') as input_file:
            for line in input_file:
                for char in line:
                    output_file.write(to_ord(char))
                

    time_exec = (time.time() - time_exec)
    return time_exec

def decrypt(input: str, output: str, key: str) -> float:
    time_exec = time.time()

    STEP = 4

    with open(output, '+w') as output_file:
        with open(input, 'r') as input_file:
            for line in input_file:
                for i in range(0, len(line), STEP):
                    num = line[i:i+STEP]
                    output_file.write(to_char(num))

    time_exec = (time.time() - time_exec)
    return time_exec