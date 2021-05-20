casos = int(input())
cont = int(0)
while (cont < casos):
    a, b, c = input().split(" ")
    a = float(a)
    b = float(b)
    c = float(c)
    media = float(((a * 2) + (b * 3) + (c * 5)) / 10)
    print("%.1f"%(media))
    cont = cont + 1