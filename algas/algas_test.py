import time
import csv
import psutil  # Importe psutil


def iterate(arr):
    counter = 0
    for i in arr:
        for j in range(0, i):
            counter += j


def execute_first_block(step):
    arr = []
    for i in range(10 * 5, 10**6, step):
        arr.append(i)
    iterate(arr)


def main():
    initial_step = 10**6
    step = initial_step
    tempo = []
    step_arr = []
    memory_usage = []

    while True:
        inicio = time.time()
        execute_first_block(step)
        fim = time.time()
        time_result = round(fim - inicio, 2)

        print(f"Tempo: {time_result}")
        print(f"Step: {step}")

        tempo.append(time_result)
        step_arr.append(step)

        memory_usage.append(psutil.Process().memory_info().rss)

        step -= int(step * 0.1)

        if step < 100:
            print("Step chegou a um valor muito baixo.")
            break

    save_to_csv(step_arr, tempo, memory_usage)


def save_to_csv(x, y, memory):
    with open("data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["Tamanho do step (n)", "Tempo gasto", "Uso de Memória (bytes)"]
        )
        for i in range(len(x)):
            writer.writerow([x[i], y[i], memory[i]])


if __name__ == "__main__":
    main()
