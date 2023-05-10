# -*- coding: utf-8 -*-
# 演習1（forのネスト）
# 1から31までの整数を要素とするリスト1と，1から12までの整数を要素とするリスト2を作成します．
# リスト1とリスト2から値を1つずつ取ってきた時，1の位が一致する値が何組あるかを求めてください．
# 例えば，1と11は，1の位が両方1なので，カウントに入ります．1と1，31と1なども同様です．
list1 = list(range(1, 32))
list2 = list(range(1, 13))
count = 0
for num1 in list1:
    target_num1 = num1 % 10
    for num2 in list2:
        if target_num1 == num2 % 10:
            count += 1
print(count)
