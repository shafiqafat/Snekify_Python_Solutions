A = int(input())
B = int(input())
if A<B:
    for _ in range(A, B+1):
        print(_, end=" ")
else:
    for _ in range(A, B-1, -1):
        print(_, end=" ")
