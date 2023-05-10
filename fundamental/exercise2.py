# 辞書が以下のように定義されています．
dic = {'two':324, 'four':830, 'three':493, 'one':172, 'five':1024}
# この時，値で昇順ソートしたと考えた場合のキーの並びを出力してください

sorted_dic = sorted(list(dic.items()), key=lambda x: x[1])
print([item[0] for item in sorted_dic])