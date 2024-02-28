routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]
answer = 0 
routes.sort(reverse=True)
last_camera = 30001

for r in routes:
  s,e = r
  if last_camera > e:
    answer +=1
    last_camera = s 
return answer
