from sum import add
from difference import subtract


def shift(sum, multiplier):
    last = multiplier[-1]
    multiplier = sum[-1]+multiplier[:-1]
    sum = sum[0]+sum[:-1]
    return sum, multiplier, last


def product(n1, n2, n):
    sum = "".zfill(n)
    last = '0'
    for i in range(n):
        if(n2[len(n2)-1] == '1' and last == '0'):
            sum = subtract(sum, n1, n)
        elif(n2[len(n2)-1] == '0' and last == '1'):
            sum = add(sum, n1, n)
            if(len(sum) > n):
                sum = sum[1:]
        sum, n2, last = shift(sum, n2)
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
