# 今，文字列が以下のように与えられています．
doc = 'i bought an apple .\ni ate it .\nit is delicious .'
# \nは改行記号なので，3つの文が3行に渡って書かれていることになります．
# この文章中の単語を用いて，キーとして単語，値として出現数を持つような辞書word2freqを作成し，
# 出力してください．ただし，改行記号は単語に含めないでください．
array_doc = doc.replace("\n", " ").split(" ")
word2freq = {}
for word in array_doc:
    word2freq[word] = word2freq.get(word, 0) + 1
print(word2freq)