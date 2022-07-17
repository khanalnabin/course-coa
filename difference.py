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
    if len(result) > n:
        return result[1:]
    else:
        return "-"+twos_complement(result, n)
