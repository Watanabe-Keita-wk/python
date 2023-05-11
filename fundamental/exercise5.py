# 2つの集合A,Bの類似度を計算する方法として，Jaccard係数というものがあります．例えば，文章の類似度の指標として使われています．

# Jaccard(A,B)=|A∩B|/|A∪B|
# 2つのリストが与えられている時，リストを集合と見なした時のJaccard係数の値を求めてください

list1 = [12,23,34,45,56,67,78,89]
list2 = [21,32,43,45,65,67,78,98]

a_and_b = 0
for num1 in list1:
    if num1 in list2:
        a_and_b += 1
a_or_b = len(list1) + len(list2) - a_and_b
jaccard = a_and_b / a_or_b

print(jaccard)