import matplotlib.pyplot as plt
from collections import deque
import random
import time


def bubble_sort(arr):
    n = len(arr)
    # Percorre todos os elementos do array
    for i in range(n):
        # Últimos i elementos já estão no lugar certo, então não precisamos mais verificar eles
        for j in range(0, n - i - 1):
            # Percorre o array de 0 a n-i-1
            # Troca se o elemento atual for maior que o próximo
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# MAX NO. OF POINTS TO STORE
que = deque(maxlen=40)


numero = 10
while True:
    # GENERATING THE POINTS - FOR DEMO
    inicio = time.time()
    bubble_sort(list(range(numero)))
    fim = time.time()
    que.append(round(fim - inicio, 2))

    # PLOTTING THE POINTS
    plt.plot(que)
    plt.scatter(range(len(que)), que)

    # SET Y AXIS RANGE
    plt.ylim(0, 1)

    # DRAW, PAUSE AND CLEAR
    plt.draw()
    plt.pause(0.1)
    plt.clf()
    numero *= 3
    time.sleep(0.5)
