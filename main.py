from memory_profiler import memory_usage
import time
import random
import sys

sys.setrecursionlimit(99999)


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


if __name__ == "__main__":
    original_arr = list(range(100))
    arr = random.sample(original_arr, len(original_arr))

    inicio = time.time()
    memoria, (resultado, ciclos) = memory_usage(
        (bubble_sort, (arr.copy(),), {}), max_usage=True, retval=True
    )
    fim = time.time()

    tempo_total = fim - inicio

    print(f"Uso máximo de memória: {memoria}")
    print(f"Ciclos: {ciclos}")
    print(f"Tempo: {tempo_total}")

    r = random.sample(original_arr, len(original_arr))

    i = time.time()
    memoria2, resultado2 = memory_usage(
        (quick_sort, (r, 0, len(arr) - 1), {}),
        max_usage=True,
        retval=True,
    )
    f = time.time()

    tt = f - i

    print(f"Uso máximo de memória: {memoria2}")
    print(f"Tempo: {tt}")
