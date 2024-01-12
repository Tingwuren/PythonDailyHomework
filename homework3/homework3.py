shakes = open('./shakespeare.txt') # 打开文本文件，位于当前项目目录下
text = shakes.read() # 获取文本
words = text.split()[:1200] # 用空格分隔得到单词列表

# 按首字母对单词列表进行分类
word_dict = {}
word_dict = dict.fromkeys('abcdefghijklmnopqrstuvwxyz') # 初始化单词字典
# 遍历单词列表中的单词
for word in words:
    word = word.lower() # 将单词变为小写
    first_letter = word[0] # 取出单词首字母
    # 跳过标点符号
    if first_letter.isalpha() is False:
        continue
    # 字典中有了首字母索引则扩充列表
    if word_dict[first_letter] != None:
        word_dict[first_letter].append(word)
    # 字典无首字母索引则新建索引
    else:
        word_dict[first_letter] = [word]

# 计算每个分类中单词的个数（重复的单词不计算入内）
count_dict = {}
# 遍历单词字典
for letter, word_list in word_dict.items():
    if word_list != None:
        count_dict[letter] = len(set(word_list)) # 将单词列表转变为无序不允许重复的集合来统计单词个数
    else:
        count_dict[letter] = 0

# 输出每个分类中单词的个数
print('a）字母“a”到“z”，每个分类中单词的个数（重复的单词不计算入内）:') 
for letter, count in count_dict.items():
    print(letter + ' : ' + str(count))
print()

# 计算在文本中出现的次数最多的10个单词及出现频次
word_count = {}
for letter, word_list in word_dict.items():
    if word_list == None:
        continue # 如果单词列表为空则跳过
    # 遍历单词列表
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

# 输出出现频次最多的10个单词及出现频次
print('b）在本文中出现的次数最多的10个单词及出现频次：')
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_word_count[:10]:
    print(word + " : " + str(count))