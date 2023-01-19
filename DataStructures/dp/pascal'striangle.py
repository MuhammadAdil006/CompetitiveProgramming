def pascal(n):
    output = [[1]]
    pre = []
    for i in range(2, n+1):
        cur = [1]
        for j in range(len(pre)-1):
            cur.append(pre[j]+pre[j+1])

        cur.append(1)
        output.append(cur)
        pre = cur
    return output


print(pascal(5))
