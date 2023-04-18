# -*- coding: utf-8 -*-
# 31. スライス2
a = 'understand'
print(a[1::2])

# 32. スライス3
b = [1,2,3,4,5]
print(b[::-1])

# 33. 集合
c = [1,1,2,3,3,4,5]
print(set(c))

# 34. 積集合
d = {1,2,3,4,5}
e = {3,4,5,6,7}
print(set(d & e))

# 35. 和集合
print(set(d | e))

# 36. 差集合
print(set(d - e))

# 37. 型の確認
f = {'A':1, 'B':2}
g = "hoge"
h = {1,2,3,4,5}
print(type(f))
print(type(g))
print(type(h))

# 38. strip
i = 'This is sentence .\n'
print(i.rstrip())

# 39. split
j = 'C C++ // python java'
print(j.split(' '))
print(j.split('/'))

# 40. join
k = ['This', 'is', 'a', 'sentence']
print(' '.join(k))