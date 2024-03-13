def solution(tickets):
    answer = []
    stack = [("ICN",[],["ICN"])]
    while stack:
        now,visited,s  = stack.pop()
        f = True
        for t in range(len(tickets)):
            if t in visited:
                continue
            st,ed = tickets[t]
            if now == st:
                stack.append((ed,visited+[t],s+[ed]))
                f = False
        if f and len(s)== len(tickets)+1:
            answer.append(s)
    #print(answer)
    answer.sort(key=lambda x: "".join(x))
    return answer[0]
