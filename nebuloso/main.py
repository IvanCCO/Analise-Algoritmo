def left(i: int) -> int:
    return 2 * i + 1


def right(i: int) -> int:
    return 2 * i + 2


def heapify(a: list, n: int, i: int):
    e = left(i)
    d = right(i)
    mx = 0
    aux = 0

    if e < n - 1 and a[e] > a[i]:
        mx = e
    else:
        mx = i

    if d < n - 1 and a[d] > a[mx]:
        mx = d

    if mx != i:
        aux = a[i]
        a[i] = a[mx]
        a[mx] = aux
        heapify(a, n, mx)


def buildHeap(a: list, n: int):
    i = n // 2 - 1

    for j in range(i, -1, -1):
        heapify(a, n, j)


if __name__ == "__main__":
    arranjo = [2, 5, 8, 13, 21, 1, 3, 34]
    buildHeap(arranjo, 8)
    print(arranjo)
