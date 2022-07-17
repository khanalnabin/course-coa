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
