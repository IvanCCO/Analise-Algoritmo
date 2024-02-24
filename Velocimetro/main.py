import time
import sys
from datetime import datetime
from memory_profiler import memory_usage
import matplotlib.pyplot as plt
import numpy as np
import random
import math


def sum_of_n_init(n):
    acumulator = 0
    for i in range(1, n):
        acumulator += i
    return acumulator


def multilply_by_minute() -> int:
    now = datetime.now().time().minute
    if now <= 0:
        return 1
    return now


def multilply_by_hour() -> int:
    now = datetime.now().time().hour
    if now <= 0:
        return 1
    return now


def multilply_by_seconds() -> int:
    now = datetime.now().time().second
    if now <= 0:
        return 1
    return now


def multilply_by_microseconds() -> int:
    now = datetime.now().time().microsecond
    if now <= 0:
        return 1
    return now


def separator():
    print("=" * 100)


def plot_grafico_de_linha_2(y1, x1):
    while True:
        plt.plot(
            x1, y1, label="sum_of_n_init"
        )  # Linha para o primeiro conjunto de dados
        plt.xlabel("Tamanho do input (n)")
        plt.ylabel("Tempo gasto")
        plt.title("Gráfico de Linha")
        plt.legend(
            "Demostrando como ao aumentar o tamanho de N de forma não linear impacta no desempenho do algoritmo"
        )
        plt.show()


if __name__ == "__main__":
    tempo_y = []
    x = []
    counter = 0

    m = 1
    n = 1

    try:
        while True:
            num = max(m, n)
            m = random.randint(num, (num + random.randint(1, num)))
            n = random.randint(num, (num + random.randint(1, num)))
            if multilply_by_minute() > 30:
                acelerador = m * n * random.randint(1, 100)
            else:
                acelerador = m * n

            print(f"Valores de multiplicação serão {m} * {n}")
            inicio = time.time()
            sum_of_n_init(acelerador)
            fim = time.time()
            tempo = round(fim - inicio, 2)
            tempo_y.append(tempo)
            x.append(acelerador)
            print(f"Acelerador = {acelerador}, tempo = {tempo}")
            counter += 1
    except Exception as e:
        print(e)
    finally:
        plot_grafico_de_linha_2(tempo_y, x)
