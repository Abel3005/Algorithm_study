def solution(name):
  answer = 0
  w = [0] + [i for i in range(len(name)) if name[i] != 'A']
  for i in w:
    a = ord(name[i]) - ord('A')
    b = a if name[i] < N else 26 - a
    answer += b
  stack = [(0,0,[0])]
  minV = int(1e9)
  while stack:
    now, su, s = stack.pop()
    t = now
    if len(s) == len(w):
      minV = su if minV > su else minV
      continue
    while True:
      left = t -1 if t > 0 else len(w) -1
      if left in s:
        t = left
      else:
        a = w[now] - w[left] if left < now else w[now] + len(name) - w[left]
        stack.append((left, su + a, s + [left]))
        break
    t = now
    while True:
      right = t + 1 if t < len(w) -1 else 0
      if right in s:
        t = right
      else:
        b = w[right] - w[now] if now < right else w[right] + len(name) - w[now]
        stack.append((right,su+b,s + [right]))
        break
answer += minV
return answer
