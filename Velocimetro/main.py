from contextlib import aclosing
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


def scatter():
    x = [
    5000001,
    10000001,
    15000002,
    20000003,
    25000005,
    30000007,
    35000010,
    40000013,
    45000017,
    50000021,
    55000026,
    60000031,
    65000037,
    70000043,
    75000050,
    80000057,
    85000065,
    90000073,
    95000082,
    100000091,
    1000000910,
    1005000920,
    1010000931,
    1015000942,
    1020000954,
    1030000979,
    1035000992,
    1040001006,
    1045001020,
    1050001035,
    1055001050,
    1060001066,
    1065001082,
    1070001099,
    1075001116,
    1080001134,
    1085001152,
    1090001171,
    1095001190,

    ]
    y1 = [
0.27
,0.55
,0.83
,1.11
,1.32
,1.59
,1.84
,2.15
,2.38
,2.66
,3.0
,3.19
,3.45
,3.68
,3.92
,4.19
,4.52
,4.77
,4.96
,5.27
,54.34
,53.6
,54.86
,54.7
,55.55
,55.82
,56.18
,55.83
,56.01
,57.25
,57.97
,58.27
,57.09
,55.17
,55.31
,55.59
,56.32
,56.67
,54.04

        ]
    y2 = [
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        69.65234375,
        
    ]
    plt.scatter(x, y1, label="Y1")
    plt.scatter(x, y2, label="Y2")

    # Adicionar rótulos aos eixos
    plt.xlabel("Eixo X")
    plt.ylabel("Eixos Y")

    # Adicionar uma legenda
    plt.legend()

    # Exibir o gráfico
    plt.show()


if __name__ == "__main__":
    scatter()
    # tempo_y = []
    # x = []
    # acelerador = 1
    # counter = 0
    # elevated = 1
    # counter = 0
    #
    # begin = 10**7
    # end = 10**7
    #
    # try:
    #     for i in range(begin, 10**8):
    #         if counter >= 20:
    #             acelerador *= 10
    #             counter = 0
    #         else:
    #             acelerador += i // 2
    #         print(f"Valores de multiplicação serão {acelerador}")
    #         inicio = time.time()
    #         sum_of_n_init(acelerador)
    #         fim = time.time()
    #         tempo = round(fim - inicio, 2)
    #         tempo_y.append(tempo)
    #         x.append(acelerador)
    #         print(f"Acelerador = {acelerador}, tempo = {tempo}")
    #         counter += 1
    # except Exception as e:
    #     print(e)
    # finally:
    #     plot_grafico_de_linha_2(tempo_y, x)
