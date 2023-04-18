# -*- coding: utf-8 -*-
# 21. リスト（forによる捜査, enumerate
a = [1,2,3,4,5]
for i, num in enumerate(a):
    if i % 2 == 0:
        print(num)

# リスト（len）
b = [11,22,33,44,55,66]
print(len(b))

# 23. リスト，if（存在確認）
if 44 in b:
    print(True)
else:
    print(False)

# 24. タプル，リストの負の添え字
c = (a[0], a[-1])
print(c)

# 25. 辞書
d = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
print(d)

# 26. 辞書（keys）
print(list(d.keys()))

# 27. 辞書（values）
print(list(d.values()))

# 28. 辞書（items）
print(list(d.items()))

# 29. 辞書（キーの存在確認）
e = {'apple':10, 'grape':20, 'orange':30}
e['apple'] = e.get('apple', -1)
e['pineapple'] = e.get('pineapple', -1)
print(e)

# 30. スライス1
f = 'training'
print(f[1:5])