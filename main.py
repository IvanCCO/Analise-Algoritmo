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
            ciclos += 1  # O(i)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, ciclos


def partition(arr, low, high):
    pivot = arr[high]  # inteiro O(1)
    i = low - 1  # inteiro (O(1))

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1  # O(1)
            # [0,1] [1, 0]
            arr[i], arr[j] = arr[j], arr[i]

    # Só troca não aloca nada
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # inteiro O(1)


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition_helder(arr, low, high):
    global cicloQuick
    # Pega o último elemento como pivô
    pivot = arr[high]

    # Índice do menor elemento
    i = low - 1

    for j in range(low, high):
        cicloQuick += 1
        # Se o elemento atual for menor ou igual ao pivô
        if arr[j] <= pivot:
            # Incrementa o índice do menor elemento
            i += 1
            # Troca arr[i] com arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Troca arr[i+1] com arr[high] (o pivô)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_helder(arr, low, high):
    if low < high:
        # Encontra o índice do pivô
        pi = partition_helder(arr, low, high)

        # Divide e conquista
        quick_sort_helder(arr, low, pi - 1)
        quick_sort_helder(arr, pi + 1, high)


def unsorted_arr(num: int):
    original_arr = list(range(num))
    arr = random.sample(original_arr, len(original_arr))
    return arr


# Analise assintótica do algoritmo
def bubble_sort_execution(i: int):
    arr = unsorted_arr(i * 1000)
    inicio = time.time()
    bubble_sort(arr)
    fim = time.time()
    tempo_total = round(fim - inicio, 2)
    print(f"tempo para executar BUBBLE SORT com {len(arr)} foi de {tempo_total}")
    del fim
    del inicio
    return tempo_total


def quick_sort_execution(i: int):
    arr = unsorted_arr(i * 1000)
    inicio = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    fim = time.time()
    tempo_total = round(fim - inicio, 2)
    print(f"tempo para executar QUICK SORT com {len(arr)} foi de {tempo_total}")
    del fim
    del inicio
    return tempo_total


def quick_sort_execution_worst(i: int):
    arr = list(range(i * 1000))
    inicio = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    fim = time.time()
    tempo_total = round(fim - inicio, 2)
    print(f"tempo para executar QUICK SORT WORST com {len(arr)} foi de {tempo_total}")
    del fim
    del inicio
    return tempo_total


def plot_grafico_de_linha_test():
    bubble_sort = [
        4950,
        499500,
        49995000,
        4999950000,
        49999500000,
    ]  # Ciclos para o Algoritmo 1 em diferentes conjuntos de dados
    quick_sort = [
        15448,
        512912,
        50565114,
        50302146,
        200,
    ]
    plt.plot(
        list(range(len(bubble_sort))), bubble_sort, label="Essa rola"
    )  # Linha para o primeiro conjunto de dados
    plt.plot(
        list(range(len(quick_sort))), quick_sort, label="Essa rola"
    )  # Linha para o primeiro conjunto de dados

    plt.xlabel("Tamanho do input (n)")
    plt.ylabel("Tempo gasto")
    plt.title("Gráfico de Linha Comparativo")
    plt.legend()
    plt.show()


def plot_grafico_de_linha_1(y1, y2, y3):
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


def plot_grafico_de_linha_2(y1, y2):
    plt.plot(
        list(range(len(y1))), y1, label="Bubble Sort O(n²)"
    )  # Linha para o primeiro conjunto de dados
    plt.plot(
        list(range(len(y2))), y2, label="Quick Sort O(n log n)"
    )  # Linha para o segundo conjunto de dados
    plt.xlabel("Tamanho do input (n)")
    plt.ylabel("Tempo gasto")
    plt.title("Gráfico de Linha Comparativo")
    plt.legend()
    plt.show()


def plot_grafico_de_linha(y1):
    plt.plot(
        list(range(len(y1))), y1, label="Bubble Sort O(n²)"
    )  # Linha para o primeiro conjunto de dados
    plt.xlabel("Tamanho do input (n)")
    plt.ylabel("Tempo gasto")
    plt.title("Gráfico de Linha Comparativo")
    plt.legend()
    plt.show()


def plot_grafico_column():
    # Dados de exemplo
    algoritmo1 = [
        100,
        150,
        200,
    ]  # Ciclos para o Algoritmo 1 em diferentes conjuntos de dados
    algoritmo2 = [
        120,
        140,
        180,
    ]  # Ciclos para o Algoritmo 2 em diferentes conjuntos de dados
    conjuntos_de_dados = ["Conjunto 1", "Conjunto 2", "Conjunto 3"]

    # Configurando as posições no eixo x para os conjuntos de dados
    posicoes = np.arange(len(conjuntos_de_dados))

    # Criando o gráfico de barras empilhadas
    plt.bar(posicoes, algoritmo1, label="Algoritmo 1")
    plt.bar(posicoes, algoritmo2, bottom=algoritmo1, label="Algoritmo 2")

    # Configurando o eixo x e adicionando rótulos
    plt.xlabel("Conjuntos de Dados")
    plt.ylabel("Quantidade de Ciclos")
    plt.title("Comparação de Ciclos entre Algoritmo 1 e Algoritmo 2")
    plt.xticks(posicoes, conjuntos_de_dados)
    plt.legend()

    # Exibindo o gráfico
    plt.show()


def plot_grafico_columns_test():
    bubble_sort = [
        # 4950,
        # 499500,
        4995000,
        # 49950000,
        # 499500000,
        # 4995000000,
    ]  # Ciclos para o Algoritmo 1 em diferentes conjuntos de dados
    quick_sort = [
        # 576,
        # 11989,
        163894,
        # 1991240,
        # 24797958,
        # 296718117,
    ]  # Ciclos para o Algoritmo 2 em diferentes conjuntos de dados
    conjuntos_de_dados = [
        # "100(cem)",
        # "1_000(mil)",
        "10_000(dez mil)",
        # "100_000(cem mil)",
        # "1_000_000(um milhão)",
        # "10_000_000(Dez milhões)",
    ]

    # Configurando as posições no eixo x para os conjuntos de dados
    posicoes = np.arange(len(conjuntos_de_dados))

    # Configurando a largura das barras
    largura_barras = 0.25

    # Criando o gráfico de barras agrupadas
    plt.bar(
        posicoes - largura_barras / 2, bubble_sort, largura_barras, label="Bubble sort"
    )
    plt.bar(
        posicoes + largura_barras / 2, quick_sort, largura_barras, label="Quick sort"
    )

    # Configurando o eixo x e adicionando rótulos
    plt.xlabel("Tamanho do input (N)")
    plt.ylabel("Quantidade de Ciclos")
    plt.title("Comparação de ciclos entre os algoritmos")
    plt.xticks(posicoes, conjuntos_de_dados)
    plt.legend()

    # Exibindo o gráfico
    plt.show()


def sepator():
    print("=" * 100)


if __name__ == "__main__":
    tempo_y_bs = []
    tempo_y_qs = []
    tempo_y_qs_w = []
    sys.setrecursionlimit(10**9)
    random.seed(10)
    #
    try:
        for i in range(1, 1_000_000):
            tempo_y_bs.append(bubble_sort_execution(i))
            tempo_y_qs.append(quick_sort_execution(i))
            tempo_y_qs_w.append(quick_sort_execution_worst(i))
            sepator()
    except Exception as e:
        print(e)
    finally:
        while True:
            plot_grafico_de_linha_1(tempo_y_bs, tempo_y_qs, tempo_y_qs_w)
