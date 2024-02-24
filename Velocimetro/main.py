import time
import sys
from datetime import datetime
from memory_profiler import memory_usage
import matplotlib.pyplot as plt
import numpy as np


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


def separator():
    print("=" * 100)


def plot_grafico_de_linha_2(y1, y2):
    while True:
        plt.plot(
            list(range(len(y1))), y1, label="sum_of_n_init"
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
    memoria_y = []
    multiplicator = 1
    counter = 0
    try:
        while True:
            if counter > 500:
                counter = 0
                multiplicator += multiplicator
            cicle = multilply_by_minute() * multilply_by_hour() * multiplicator
            inicio = time.time()
            sum_of_n_init(cicle)
            fim = time.time()
            tempo = round(fim - inicio, 2)
            tempo_y.append(tempo)
            # memoria_y.append(memoria)
            print(f"Tempo gasto para percorrer {cicle} iterações = {tempo}")
            counter += 1
    except Exception as e:
        print(e)
    finally:
        plot_grafico_de_linha_2(tempo_y, memoria_y)
