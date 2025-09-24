#!/usr/bin/python3

import  aes, substitution, columnar, os, pandas as pd
import matplotlib.pyplot as plt

files_list = ['./clear_text/1-LoremIpsum.txt', './clear_text/2-Frankenstein.txt', './clear_text/3-CompleteWorksShakespeare.txt']

key: str = input("Insira sua chave: ")
second_key: str = input("Insira sua segunda chave: ")
times = [[],[],[]]
i = 0
for file in files_list:
    aes_encrypt_file = file+'.aes'
    aes_decrypt_file = file+'.aes.dec'
    students_encrypt_file = file+'.est'
    students_decrypt_file = file+'.est.dec'

    times[i].append(('AES - Enc', aes.encrypt(file, aes_encrypt_file, key)))
    times[i].append(('AES - Dec', aes.decrypt(aes_encrypt_file, aes_decrypt_file, key)))

    encrypt_time = columnar.encrypt(file, key, second_key)
    encrypt_time += substitution.encrypt(students_encrypt_file, key)
    times[i].append(('Students - Enc', encrypt_time))

    decrypt_time = substitution.decrypt(students_encrypt_file, key)
    decrypt_time += columnar.decrypt(students_decrypt_file, key, second_key)
    times[i].append(('Students - Dec', decrypt_time))
    i += 1

# Create 3 different DataFrames, one per row of times
df1 = pd.DataFrame(times[0], columns=['Operation', 'Time (seconds)'])
df1['File'] = files_list[0]

df2 = pd.DataFrame(times[1], columns=['Operation', 'Time (seconds)'])
df2['File'] = files_list[1]


df3 = pd.DataFrame(times[2], columns=['Operation', 'Time (seconds)'])
df3['File'] = files_list[2]



# Create and export plots for each DataFrame
def create_plot(df, title, filename):
    if not df.empty:
        plt.figure(figsize=(12, 8))
        bars = plt.bar(df['Operation'], df['Time (seconds)'], color=['skyblue', 'lightcoral', 'lightgreen', 'orange'])
        plt.title(f'Encryption/Decryption Times - {title}', fontsize=14)
        plt.xlabel('Operation', fontsize=12)
        plt.ylabel('Time (seconds) - Log Scale', fontsize=12)
        plt.yscale('log')  # Use logarithmic scale
        plt.xticks(rotation=45)
        
        # Add value labels on top of bars
        for bar, value in zip(bars, df['Time (seconds)']):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), 
                    f'{value:.4f}', ha='center', va='bottom', fontsize=10)
        
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Plot saved as: {filename}")
    else:
        print(f"No data to plot for {title}")

# Create plots for each DataFrame
create_plot(df1, "LoremIpsum", "10kb file")
create_plot(df2, "Frankenstein", "500kb file")
create_plot(df3, "Complete Works Shakespeare", "5mb file")

print(times)
os.remove('intermed.txt')