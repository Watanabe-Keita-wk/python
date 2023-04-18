# -*- coding: utf-8 -*-
# 1.変数
a = 2
print(a * 3)

# 2.swap
b = 100
c = 200
b, c = c, b
print("b, c = {}, {}".format(b, c))

# 3.四則演算+α
d = 10
e = 2
print("和：{}".format(d + e))
print("差：{}".format(d - e))
print("積：{}".format(d * e))
print("商：{}".format(d / e))

# 4.余り
f = 5
g = 3
print(f % g)

# 5.べき乗
h = 5
i = 10
print(h ** i)

# 6.if，比較演算子<, >
j = 5
k = 10
if j > k:
    print(j)
else:
    print(k)

# 7.比較演算子==, bool
l = 5
print(l % 2 == 0)

# 8.文字列（ランダムアクセス）
m = "python"
print(m[2])

# 9.文字列（結合）
n = "py"
o = "thon"
print(n + o)

# 10.文字列（format）
p = 5
q = 3
print("{}%{}={}".format(p, q, p%q))