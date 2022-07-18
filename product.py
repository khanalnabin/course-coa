from sum import add


def shift(char, original):
    return char + original[:len(original)-1]


def product(n1, n2, n):
    sum = "".zfill(n)
    for i in range(n):
        if(n2[len(n2)-1] == '1'):
            sum = add(sum, n1, n)
        n2 = shift(sum[len(sum)-1], n2)
        sum = sum[:len(sum)-1].zfill(n)
    return sum, n2


def main():
    n = int(input("Enter the number of bits: "))

    n1 = input("Enter the first number: ")
    n2 = input("Enter the second number: ")

    n1 = n1.zfill(n)
    n2 = n2.zfill(n)

    print(product(n1, n2, n))


if (__name__ == "__main__"):
    main()
