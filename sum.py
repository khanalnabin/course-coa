def add(s1, s2, n):
    result = ""
    carry = False
    for i in range(n-1, -1, -1):
        a = s1[i]
        b = s2[i]
        if (a == "1" and b == "0" or a == "0" and b == "1"):
            if carry:
                result = '0' + result
            else:
                result = '1'+result
        else:
            if (a == '0' and b == '0'):
                if (carry):
                    result = '1' + result
                    carry = False
                else:
                    result = '0' + result
            else:
                if carry:
                    result = '1'+result
                else:
                    result = '0' + result
                    carry = True

    if carry:
        result = '1' + result

    return result
