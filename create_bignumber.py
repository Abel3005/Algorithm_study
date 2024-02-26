def solution(number, k):
    stack = [number[0]]
    for i in number[1:]:
        while len(stack) > 0 and stack[-1] < i and k >0:
            k -= 1
            stack.pop()
        stack.append(i)
    answer = ("".join(stack))
    answer = answer[:len(answer)-k]
    return answer
