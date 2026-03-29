import jieba

ls = jieba.lcut("国家计算机二级考试Python学科") #精确模式
print(ls)

ls = jieba.lcut("国家计算机二级考试Python学科",cut_all = True) #全模式
print(ls)

ls =jieba.lcut_for_search("国家计算机二级考试Python学科") #搜索模式
print(ls)

jieba.add_word("Python学科")
ls = jieba.lcut("国家计算机二级考试Python学科")
print(ls)
