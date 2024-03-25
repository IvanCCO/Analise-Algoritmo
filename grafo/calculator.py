def binary_addition(a, b):
    a_bin = bin(a)[2:].zfill(4)
    b_bin = bin(b)[2:].zfill(4)

    print(f"A: {a} -> {a_bin}")
    print(f"B: {b} -> {b_bin}")

    carry = 0
    result = ""

    for i in range(min(len(a_bin), len(b_bin)) - 1, -1, -1):
        bit_a = int(a_bin[i])
        bit_b = int(b_bin[i])
        sum_bits = bit_a ^ bit_b ^ carry
        carry = (bit_a & bit_b) | (bit_a & carry) | (bit_b & carry)

        result = str(sum_bits) + result

    if carry:
        result = "1" + result

    print(f"{a} + {b} = {result}\n")
    return result


while KeyboardInterrupt:
    result = binary_addition(int(input("A: ")), int(input("B: ")))
