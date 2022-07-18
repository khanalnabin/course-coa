from difference import subtract


def shift(A, Q):
    return A[1:]+Q[0], Q[1:]+'_'


def divide(dividend, divisor, n):
    A = "".zfill(n)
    Q = dividend
    M = divisor
    for i in range(n):
        # print("Unshifted: ", A, Q)
        A, Q = shift(A, Q)
        # print("shifted: ", A, Q)
        sub = subtract(A, M, n)
        # print("Subtract result: ", sub)
        if (sub[0] == '1'):
            Q = Q[:len(Q)-1]+'0'
        else:
            A = sub
            Q = Q[:len(Q)-1]+'1'
    return Q, A


def main():

    n = int(input("Enter the number of bits: "))

    n1 = input("Enter the first number: ")
    n2 = input("Enter the second number: ")

    n1 = n1.zfill(n)
    n2 = n2.zfill(n)
    print(divide(n1, n2, n))


if(__name__ == '__main__'):
    main()
