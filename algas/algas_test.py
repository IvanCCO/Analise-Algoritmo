import time
import csv


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
    max_time = 10  # Tempo máximo desejado
    tempo = []
    step_arr = []

    while True:
        inicio = time.time()
        execute_first_block(step)
        fim = time.time()
        time_result = round(fim - inicio, 2)

        print(f"Tempo: {time_result}")
        print(f"Step: {step}")

        tempo.append(time_result)
        step_arr.append(step)

        step -= int(step * 0.1)

        if step < 1:
            print("Step chegou a um valor muito baixo.")
            break

    save_to_csv(step_arr, tempo)


def save_to_csv(x, y):
    with open("data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Tamanho do step (n)", "Tempo gasto"])
        for i in range(len(x)):
            writer.writerow([x[i], y[i]])


if __name__ == "__main__":
    main()
