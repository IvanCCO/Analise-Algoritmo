from sys import _current_frames
import time
import matplotlib.pyplot as plt
import numpy as np


# a) range (100000, 600000, 100000)
# b) range (1000, 6000, 100)
# c) range (100, 600, 100)
# d) range (10, 60, 10)
# e) range (1000000, 6000000, 1000000
def iterate(arr):
    counter = 0
    for i in arr:
        for j in range(0, i):
            counter += j


def execute_first_block(step):
    arr = []
    for i in range(100000, 600000, step):
        arr.append(i)
    iterate(arr)


def main():
    step = 100000

    tempo = []
    step_arr = []
    while True:
        inicio = time.time()
        execute_first_block(step)
        fim = time.time()
        time_result = round(fim - inicio, 2)
        print(f"Tempo: {time_result}")
        print(f"Step :{step} for step")
        tempo.append(time_result)
        step_arr.append(step)
        step -= int(step * 0.1)
        if time_result > 20:
            break
    plot_grafico_de_linha_2(step_arr, tempo)


def plot_grafico_de_linha_2(x, y):
    while True:
        plt.plot(x, y, label="Tempo step")  # Linha para o segundo conjunto de dados
        plt.xlabel("Tamanho do input (n)")
        plt.ylabel("Tempo gasto")
        plt.title("Gráfico de Linha Comparativo")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    main()
