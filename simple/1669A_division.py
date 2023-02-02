cases = int(input().rstrip())
inp = []
for I in range(cases):
    inp.append(int(input().rstrip()))


def solve(rating):
    if rating >= 1900:
        return "Division 1"
    elif rating >= 1600:
        return "Division 2"
    elif rating >= 1400:
        return "Division 3"
    else:
        return "Division 4"


for J in range(cases):
    print(solve(inp[J]))
