import liruobin

# 测试函数一
print("测试函数一：")
# 定义两个测试字典  
dict1 = {"a": 1, "b": 2, "c": "3", "d": True}
dict2 = {"b": 3, "c": "4", "d": False, "e": 5}
# 调用dict_add函数并打印结果  
print(liruobin.dict_add(dict1, dict2))
# {'a': 1, 'b': 5, 'c': '34', 'd': False, 'e': 5}

# 测试函数二
print("测试函数二：")
dict = {"zero": "0", "one": "1", "two": "2", "three": "3","four": "4"} #构造待切片的字典
#调用切片方法
newdict = liruobin.dict_cut(dict, 1, 3)
print(newdict)
#{"one": "1", "two": "2"}，下标从0开始，含开头不含结尾

# 测试函数三
print("测试函数三：")
print(liruobin.compare_two_digits(3.14, 3.15)) # False
print(liruobin.compare_two_digits(3.141, 3.142)) # True
print(liruobin.compare_two_digits(3.139, 3.140)) # False
print(liruobin.compare_two_digits(3.141, 3.142)) # True

# 测试函数四
print("测试函数四：")
print(liruobin.sum_digits(2023))
# 7

# 测试函数五
print("测试函数五：")
print(liruobin.count([1, 2, 1, 2, 1], 1))
# 3