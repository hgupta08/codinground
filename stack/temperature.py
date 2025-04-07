def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []  # pair: [temp, index]

    for i, t in enumerate(temperatures):
        print(i,t)
        print(stack)
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = i - stackInd
        stack.append((t, i))
    return res

temperatures = [30,38,30,36,35,40,28]
print(dailyTemperatures(temperatures))