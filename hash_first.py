phone_book = ["119", "97674223", "1195524421"]

m = {}
answer = True
for i in phone_book:
    m[i] = 1
for i in phone_book:
    c = ""
    for j in i:
        c +=j
        if c in m and c is not i:
            answer = False
            break
print(answer)