def countBits(n):
    mem = {}
    mem[0] = 0
    mem[1] = 1
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    mem[2] = 1
    for i in range(3, n+1):
        mem[i] = i % 2+mem[i//2]
    return list(mem.values())


print(countBits(1))
