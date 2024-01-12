def dict_add(dict1, dict2):
    result = {}

    # 遍历第一个字典
    for key, value in dict1.items():
        if key in dict2:  # 如果第二个字典中也有这个键
            # 因为isinstance(True, int) and isinstance(False, int) is True，所以把bool类型放在最前面判断
            if isinstance(value, bool) or isinstance(dict2[key], bool):  # 如果一个值是布尔值
                result[key] = value and dict2[key]
            elif isinstance(value, (int, float)) and isinstance(dict2[key], (int, float)):  # 如果两个值都是数字
                result[key] = value + dict2[key]
            elif isinstance(value, str) and (isinstance(dict2[key], (int, float, str))):  # 如果前一个是字符串，后一个是数字或字符串
                result[key] = value + str(dict2[key])
            elif isinstance(value, (int, float, str)) and (isinstance(dict2[key], str)):  # 如果前一个是数字或字符串，另一个是数字
                result[key] = dict2[key] + str(value)
            
        else:  # 如果第二个字典中没有这个键
            result[key] = value

    # 遍历第二个字典，处理只在第二个字典中存在的键
    for key, value in dict2.items():
        if key not in result:
            result[key] = value

    return result