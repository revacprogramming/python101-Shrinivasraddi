
def add(a, b):
    return a+b


def output(a, b, c):
    print(f"{a} + {b} is {c}")


def main():
    a =int(input("enter the numbers:"))
    b =int(input("enter the numbers:"))
    c = add(a, b)

    output(a, b, c)


if __name__ == '__main__':
    main()