# -*- coding: utf-8 -*-
# 11. 文字列（replace）
a = "some1"
a = a.replace("1", "one")
print(a)

# 12. 文字列（lower）
b = "This Is A Sentence ."
b = b.lower()
print(b)

# 13. 文字列（upper）
c = b.upper()
print(c)

# 14. 文字列（文字数）
d = "How many characters?"
print(len(d))

# 15. 文字列 → 数値
e = "34"
f = "43"
print(int(e) + int(f))

# 16. リスト
g = [1,2,3,4,5]
print(g[3])

# 17. リスト（結合）
h = [1,2,3]
i = [4,5]
print(h + i)

# 18. リスト（append）
j = [1,2,3,4,5]
j.append(6)
j.append(7)
print(j)

# 19. リスト（insert）
k = [1,2,3,4,5]
k.insert(1, 100)
print(k)

# 20. リスト（forによる捜査）
l = [1,2,3,4,5]
for num in l:
    if num % 2 == 0:
        print(num)