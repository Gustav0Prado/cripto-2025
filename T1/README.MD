# T1 Criptografia

## Objetivo

O objetivo desse trabalho é "criar" uma cifra nova utilizando as cifras aprendidas em sala de aula, sendo uma (ou mais) de substituição e uma (ou mais) de transposição. Depois, vamos comparar o tempo de execução da cifra criada com o tempo de execução do AES para os mesmos textos claros e gerar gráficos comparando ambos.

## Cifras usadas

- Cifra de substituição:
- Cifra de transposição:

## AES

Para rodar o AES, utilizamos diretamente a OpenSSL do Linux com a opção `aes-128-cbc`, ou seja, usamos o modo CBC (Cipher Block Chaining) para encriptar. Nenhuma outra alteração ou uso foi feito além dos citados.

# Medição de tempo

Para medir o tempo de cada um utilizamos a biblioteca padrão de tempo do Python, `time` e como função para medir o tempo usamos o `perf_counter()`, que ao contrário da função `time()` é melhor para o nosso caso por ser bem mais exato em cenários onde se necessita de precisão na medição de tempo.
Basicamente para medir o tempo:

- Salvamos um timestamp com `stamp = time.pref_counter()`
- Rodamos a função desejada
- Após terminar de rodar, calculamos um novo timestamp com `stamp = (time.perf_counter() - stamp)`

# Gŕaficos

Para criar os gráficos utilizamos ...
