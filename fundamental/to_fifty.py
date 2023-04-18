# -*- coding: utf-8 -*-
# 41. max
a = [11,2,7,13,5]
print(max(a))

# 42. min
print(min(a))

# 43. sum
print(sum(a))

# 44. ソート
b = [5,3,1,4,2]
print(sorted(b))
print(sorted(b, reverse=True))

# 45. ラムダ式
c = [{'a': 6, 'b': 7, 'c': 6},
    {'a': 4, 'b': 2, 'c': 3},
    {'a': 1, 'b': 5, 'c': 8}]
print(sorted(c, reverse=True, key=lambda x:x['b']))

# 46. range()
print(list(range(100)))

# 47. 内包表記
d = [5,4,3,2,1]
print([num + index for index, num in enumerate(d)])

# 48. 例外処理
e = 0
f = 5
try:
    print(e / f)
except ZeroDivisionError:
    print('zero division')

try:
    print(f / e)
except ZeroDivisionError:
    print('zero division')

# 49. ビット演算
g = 10
h = 5
print(g | h)
print(g & h)
print(g ^ h)

# 50. モジュールのインポート
import math
i = math.pi / 2
print(math.sin(i)**2 + math.cos(i)**2)