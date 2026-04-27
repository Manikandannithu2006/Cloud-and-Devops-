def count_ways(n):
    if n <= 1:
        return 1
    
    prev2, prev1 = 1, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    
    return prev1

for i in range(1, 5):
    print(count_ways(i))
