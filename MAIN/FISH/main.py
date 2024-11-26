n, m = map(int, input().split())
x = [0] * (n + 1)
y = [0] * (m + 1)
a = [[0] * (m + 1) for _ in range(n + 1)]

x[1:] = map(int, input().split())
y[1:] = map(int, input().split())

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, m + 1):
        a[i][j] = row[j - 1] + a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1]

res = 0

for x1 in range(1, n + 1):
    for x2 in range(x1, n + 1):
        Min = float('inf')
        val = 0
        d = x[x2] - x[x1]
        for j in range(1, m + 1):
            Min = min(Min, val - d * y[j])
            val = a[x2][j] - a[x2][0] - a[x1-1][j] + a[x1-1][0]
            res = max(res, val - d * y[j] - Min)

print(res)
