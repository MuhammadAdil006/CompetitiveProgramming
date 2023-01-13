def differentways(expression):
    def helper(expression, dic):
        if expression in dic:
            return dic[expression]
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i in range(len(expression)):
            if expression[i] in "*+-":
                left = helper(expression[:i], dic)
                right = helper(expression[i+1:], dic)
                res += [eval(f'{x}{expression[i]}{y}')
                        for x in left for y in right]
        dic[expression] = res
        return res
