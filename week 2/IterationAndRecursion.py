# Randy Butts  CIS261  Iterative and Recursive Functionality

TEST_SET = [0, 5, 10, 25, 50, 100]


def iterativeFactorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def recursiveFactorial(n):
    if n == 1 or n == 0:
        return 1
    return n * recursiveFactorial(n - 1)


if __name__ == "__main__":
    print("Factorial results using an interactive function")
    print("=" * 47)
    for i in TEST_SET:
        print(f"{i}! = {iterativeFactorial(i)}")

    print("\n")

    print("Factorial results using an recursive function")
    print("=" * 45)
    for i in TEST_SET:
        print(f"{i}! = {recursiveFactorial(i)}")
