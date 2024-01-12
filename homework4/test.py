import homework4

# 定义两个测试字典  
dict1 = {"a": 1, "b": 2, "c": "3", "d": True}
dict2 = {"b": 3, "c": "4", "d": False, "e": 5}
# 调用dict_add函数并打印结果  
print(homework4.dict_add(dict1, dict2))
# {'a': 1, 'b': 5, 'c': '34', 'd': False, 'e': 5}

dict3 = {"a": 1, "b": 1, "c": 1}
dict4 = {"a": 2, "b": "hello", "c":True}
print(homework4.dict_add(dict3, dict4))
# {'a': 3, 'b': 'hello1', 'c': True}

dict3 = {"a": "world", "b": "world", "c": "world"}
dict4 = {"a": 2, "b": "hello", "c":True}
print(homework4.dict_add(dict3, dict4))
# {'a': 'world2', 'b': 'worldhello', 'c': True}

dict3 = {"a": True, "b": False, "c": False}
dict4 = {"a": 2, "b": "hello", "c":True}
print(homework4.dict_add(dict3, dict4))
# {'a': 2, 'b': False, 'c': False}