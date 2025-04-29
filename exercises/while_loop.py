"""
练习: while循环

描述：
在数字列表中查找第一个偶数。

请补全下面的函数，使用while循环在数字列表中查找并返回第一个偶数。
如果列表中没有偶数，则返回None。
"""

def find_first_even(numbers):
    """
    在数字列表中查找第一个偶数
    
    参数:
    - numbers: 整数列表
    
    返回:
    - 列表中的第一个偶数，如果没有偶数则返回None
    """
    # 请在下方编写代码
    index = 0  # 初始化索引为0
    while index < len(numbers):  # 当索引小于列表长度时循环
        if numbers[index] % 2 == 0:  # 检查当前数字是否为偶数
            return numbers[index]  # 如果是偶数，返回该数字
        index += 1  # 索引加1，继续检查下一个数字
    return None  # 如果循环结束仍未找到偶数，返回None
    pass 