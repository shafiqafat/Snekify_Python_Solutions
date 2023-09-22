fact = 1
add = 0
n = int(input())
for i in range(1, n+1):
    fact *= i
    add += fact
print(add)
