N,B = map(int,input().split())

n_s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

if N == 0:
    print(0)
else:
    while N > 0:
        result = n_s[N % B] + result
        N //= B

    print(result)