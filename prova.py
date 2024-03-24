import numpy as np


# Algoritmo log(n) -> binary search
# NEsse caso estou fazendo uma binary search para
# poder encontrar um número no array
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if int(arr[mid]) == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1


n = np.linspace(1, 100)

print("Array criado pelo linspace foi ")
print(n)

print(
    binary_search(
        n,
        0,
        len(n) - 1,
        int(input("Qual número deseja encontrar? / Digite apenas o inteiro\n")),
    )
)
