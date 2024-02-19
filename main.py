import time
import random
import sys
import matplotlib.pyplot as plt
import numpy as np


def bubble_sort(arr):
    n = len(arr)
    ciclos = 0

    # Percorre todos os elementos do array
    for i in range(n):
        # Últimos i elementos já estão no lugar certo, então não precisamos mais verificar eles
        for j in range(0, n - i - 1):
            ciclos += 1
            # Percorre o array de 0 a n-i-1
            # Troca se o elemento atual for maior que o próximo
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, ciclos


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def unsorted_arr(num: int):
    original_arr = list(range(num))
    arr = random.sample(original_arr, len(original_arr))
    return arr


def bubble_sort_execution(i: int):
    arr = unsorted_arr(i * 100)
    inicio = time.time()
    bubble_sort(arr)
    fim = time.time()
    tempo_total = round(fim - inicio, 2)
    print(f"tempo para executar BUBBLE SORT com {len(arr)} foi de {tempo_total}")
    del fim
    del inicio
    return tempo_total


def quick_sort_execution(i: int):
    arr = unsorted_arr(i * 100)
    inicio = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    fim = time.time()
    tempo_total = round(fim - inicio, 2)
    print(f"tempo para executar QUICK SORT com {len(arr)} foi de {tempo_total}")
    del fim
    del inicio
    return tempo_total


def quick_sort_execution_worst(i: int):
    arr = list(range(i * 100))
    inicio = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    fim = time.time()
    tempo_total = round(fim - inicio, 2)
    print(f"tempo para executar QUICK SORT WORST com {len(arr)} foi de {tempo_total}")
    del fim
    del inicio
    return tempo_total


def plot_grafico_de_linha(y1, y2, y3):
    plt.plot(
        list(range(len(y1))), y1, label="Bubble Sort O(n²)"
    )  # Linha para o primeiro conjunto de dados
    plt.plot(
        list(range(len(y2))), y2, label="Quick Sort O(n log n)"
    )  # Linha para o segundo conjunto de dados
    plt.plot(
        list(range(len(y3))), y3, label="Quick Sort worst O(n²)"
    )  # Linha para o segundo conjunto de dados

    plt.xlabel("Tamanho do input (n)")
    plt.ylabel("Tempo gasto")
    plt.title("Gráfico de Linha Comparativo")
    plt.legend()
    plt.show()


def sepator():
    print("=" * 100)


if __name__ == "__main__":
    tempo_y_bs = []
    tempo_y_qs = []
    tempo_y_qs_w = []
    sys.setrecursionlimit(10**9)
    random.seed(10)

    try:
        for i in range(1, 1_000_00):
            tempo_y_bs.append(bubble_sort_execution(i))
            tempo_y_qs.append(quick_sort_execution(i))
            tempo_y_qs_w.append(quick_sort_execution_worst(i))
            sepator()
    except Exception as e:
        print(e)
    finally:
        while True:
            plot_grafico_de_linha(tempo_y_bs, tempo_y_qs, tempo_y_qs_w)
