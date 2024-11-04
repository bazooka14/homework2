word = input()
res = word[len(word)//2] if len(word) % 2 == 1 else word[len(word)//2-1] + word[len(word)//2]
print(res)

z = 100
i = 1
