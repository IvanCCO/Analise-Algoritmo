import matplotlib.pyplot as plt
import numpy as np
import time
import random
from memory_profiler import memory_usage


def sum_of_n_init(n):
    if n < 10**3:
        n *= random.randint(1, n)
    elif n < 10**4:
        n *= random.randint(10**3, n)
    elif n < 10**5:
        n *= random.randint(10**4, n)
    elif n < 10**6:
        n *= random.randint(10**5, n)

    print(f"Aceleracao = {n}")

    acumul = 0

    for i in range(1, n + 1):
        acumul += i
    return acumul


def plot_grafico_de_linha(y1, y2):
    while True:
        plt.plot(list(range(len(y1))), y1, label="Diferenca da tempo")
        plt.plot(list(range(len(y2))), y2, label="Diferenca da memoria")
        plt.xlabel("Tamanho do input (n)")
        plt.ylabel("Tempo gasto")
        plt.title("Gráfico de Linha Comparativo")
        plt.legend()
        plt.show()


# Pegar um numero e dependendo do valor ter um valor dinamico para ele ir subindo a aceleração


def main():
    tempo = []
    memoria = []
    try:
        for i in range(100_0, 100_000_000_000):
            inicio = time.time()
            memo, resultado = memory_usage(
                (sum_of_n_init, (i,), {}), max_usage=True, retval=True
            )
            fim = time.time()
            tempo.append(round(fim - inicio, 2))
            memoria.append(memo)
    except Exception as e:
        print(tempo)
        print(memoria)
        plot_grafico_de_linha(tempo, memoria)


if __name__ == "__main__":
    main()
