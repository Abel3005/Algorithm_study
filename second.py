#this problem shock me 

def solution(numbers):
  a = list(map(str,numbers))
  b = sorted(a, key = lambda x : x*3, reverse = True)
  return str(int("".join(b)))
