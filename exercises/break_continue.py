"""
练习: break和continue语句

描述：
返回从1到n的所有非3的倍数的整数列表。

请补全下面的函数，使用continue语句跳过3的倍数。
"""

def skip_multiples_of_three(n):
    """
    返回从1到n的所有非3的倍数的整数列表
    
    参数:
    - n: 正整数上限
    
    返回:
    - 从1到n中所有不是3的倍数的整数列表
    """
    # 请在下方编写代码
    result = []  # 初始化一个空列表用于存储结果
    for i in range(1, n + 1):  # 遍历从1到n的整数
        if i % 3 == 0:  # 检查i是否是3的倍数
            continue  # 如果是3的倍数，跳过本次循环的剩余部分
        result.append(i)  # 如果不是3的倍数，将i添加到结果列表中
    return result  # 返回结果列表
    pass 