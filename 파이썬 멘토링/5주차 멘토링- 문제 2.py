n = int(input())
p = list(map(int, input().split()))

p.sort()

time = 0
total = 0

for q in p:
    time += q
    total += time

print(total)