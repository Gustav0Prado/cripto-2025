import subprocess, time

def encrypt_aes(input: str, output: str, key: str) -> float:
    bytes_key: bytes = key.encode('utf-8')

    time_exec = time.time()
    p = subprocess.Popen(f'openssl aes-128-cbc -e -in {input} -out {output} -K {bytes_key.hex()} -iv 00000000000000000000000000000000', shell=True, stderr=subprocess.DEVNULL)
    p.wait()
    time_exec = (time.time() - time_exec)

    return time_exec

def decrypt_aes(input: str, output: str, key: str) -> float:
    bytes_key: bytes = key.encode('utf-8')

    time_exec = time.time()
    p = subprocess.Popen(f'openssl aes-128-cbc -d -in {input} -out {output} -K {bytes_key.hex()} -iv 00000000000000000000000000000000', shell=True, stderr=subprocess.DEVNULL)
    p.wait()
    time_exec = (time.time() - time_exec)

    return time_exec