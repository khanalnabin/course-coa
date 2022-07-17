from difference import subtract

n = int(input("Enter the number of bits: "))


n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")

n1 = n1.zfill(n-len(n1)+1)
n2 = n2.zfill(n-len(n2)+1)

print(subtract(n1, n2, n))
