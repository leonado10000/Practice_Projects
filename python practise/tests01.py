def max_cool_partitions(arr):
    freq = {}
    res = 0
    for i in range(len(arr)-1, -1, -1):
        freq[arr[i]] = freq.get(arr[i], 0) + 1
        if freq[arr[i]] < res:
            res = freq[arr[i]]
        elif freq[arr[i]] == res:
            res = res
        else:
            res = res + 1
        print(f"Index: {i}, Element: {arr[i]}, Frequency: {freq[arr[i]]}, Result: {res}")
    return res

# Read input
t = int(input())
res = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_cool_partitions(arr))
