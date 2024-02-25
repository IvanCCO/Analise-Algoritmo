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


def get_acelerator(x, y) -> int:
    p = random.randint(x, x + 10)
    g = multilply_by_minute()
    if g % 5 == 0:
        return p**y
    p = p * g
    return p


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
    acelerador = 1
    counter = 0
    elevated_by = 2

    try:
        while True:
            if counter > 5 * 10:
                counter = 0
                elevated_by += 1
            acelerador = get_acelerator(acelerador, elevated_by)
            print(f"Valores de multiplicação serão {acelerador}")
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
