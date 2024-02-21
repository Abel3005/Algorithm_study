from collections import deque
def solution(name):
    answer = 0
    w = [0] + [i for i in range(1,len(name)) if name[i] != 'A']
    #alpha
    for i in w:
        a = ord(name[i]) - ord('A')
        co = a if name[i] < 'N' else 26 - a
        answer += co
  #move
  ## q (idx, list: 거쳐온 점)
    q = deque()
    q.append((0,0,[]))
    costmap = []
    while q:
        now, c, s = q.popleft()
        if len(s) == len(w)-1:
            costmap.append(c)
            continue
        lnow, rnow = now,now
        while True:
            left = lnow -1 if lnow > 0 else len(w) -1
            if left in s:
                lnow = left
                #print(lnow)
            else:
                c1 = w[now] - w[left] if now > left else w[now] + len(name)-w[left]
                q.append((left,c+c1,s+[lnow]))
                break
        while True:
            right = rnow +1 if rnow < len(w) -1  else 0
            if right in s:
                rnow = right
                #print(w)
            else:
                c2 = w[right] - w[now] if right > now else w[right] + len(name) -w[now]
                q.append((right,c+c2,s + [rnow]))
                break
    answer += min(costmap)
