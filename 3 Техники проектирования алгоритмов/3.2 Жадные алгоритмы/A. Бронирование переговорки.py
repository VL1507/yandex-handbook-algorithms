n = int(input())

intervals = []
for _ in range(n):
    l, r = map(int, input().split())  # noqa: E741
    intervals.append((l, r))

intervals.sort(key=lambda x: x[1])

k = 1
current_interval = intervals[0]

for interval in intervals[1:]:
    if interval[0] > current_interval[1]:
        k += 1
        current_interval = interval

print(k)
