# 函数一：homework4中的两个字典相加函数
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

# 函数二：字典伪切片
def dict_cut(dict, start, end):
    temp = list(dict.keys()) #临时存放字典的key
    result = {} #定义要返回的字典
    temp = temp[start:end] #利用列表的切片功能，切列表里的key
    for i in range(len(temp)):#用切完后的key列表对新的字典赋值
        result[temp[i]] = dict.get(temp[i])#从传入字典中取值
    return result#循环完成的时候，即完成了切片后字典的构造

# 函数三：封装math里面近似相等函数，实现：如果两个数小数点后两位相等，返回True，否则返回False。
import math # 导入math模块

def compare_two_digits(a, b):
    a_turnc = math.trunc(a*100) # 去除a*100的小数部分
    b_turnc = math.trunc(b*100) # 去除b*100的小数部分
    return a_turnc == b_turnc # 返回两个整数的比较结果

# 函数四：计算一个整数每一位的和
def sum_digits(n):
    if n < 10:
        return n # 如果是个位数，则返回n自己
    else: # 如果大于10，则返回整数去掉个位的后每一位和加上个位
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last
    
# 计算一个列表s中value的个数
def count(s, value):
    total = 0 # 初始化为0
    for i in range(len(s)): # 遍历列表
        if value == s[i]:
            total += 1 # 如果相等则将结果加1
    return total # 返回结果