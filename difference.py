from sum import add


def twos_complement(n1, n):
    result = ""
    for i in n1:
        if(i == "1"):
            result = result + "0"
        else:
            result = result + "1"

    result = add(result, "1".zfill(n), n)
    return result


def subtract(s1, s2, n):
    result = add(s1, twos_complement(s2, n), n)
    if(len(result) > n):
        return result[1:]
    return result


def main():
    n = int(input("Enter the number of bits: "))

    n1 = input("Enter the first number: ")
    n2 = input("Enter the second number: ")

    n1 = n1.zfill(n-len(n1)+1)
    n2 = n2.zfill(n-len(n2)+1)

    print(subtract(n1, n2, n))


if (__name__ == "__main__"):
    main()
