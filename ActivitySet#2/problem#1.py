def add(a, b):
    return a+b


def main():
    a = float(input())
    b = float(input())

    c = add(a, b)
    print(f"sum of {a} and {b} is {c}")
main()