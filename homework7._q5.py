
def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a


def phi(n):
    relatively_prime = []

    for k in range(1, n):
        if gcd(n, k) == 1:
            relatively_prime.append(k)

    return relatively_prime


def main():
    n = int(input("Enter a positive integer: "))

    if n < 1:
        print("Please enter a positive integer.")
        return

    numbers = phi(n)

    print("Numbers relatively prime to", n, ":")
    print(numbers)
    print("Euler's totient value is:", len(numbers))


main()
