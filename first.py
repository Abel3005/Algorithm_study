#first git uploadfile in this study project

# eliminate 
def solution(arr):
  answer = []
  for i in arr:
    if len(answer) == 0:
      answer.append(i)
    elif answer[len(answer)-1] != i:
      answer.append(i)
return answer
