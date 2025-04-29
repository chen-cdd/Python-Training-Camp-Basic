"""
练习: for循环

描述：
计算从1到n的所有整数之和。

请补全下面的函数，使用for循环计算从1到n的所有整数之和。
"""

def sum_numbers(n):
    """
    计算从1到n的所有整数之和
    
    参数:
    - n: 正整数
    
    返回:
    - 从1到n的所有整数之和
    """
    # 请在下方编写代码
    total_sum = 0  # 初始化总和为0
    for i in range(1, n + 1):  # 遍历从1到n的整数
        total_sum += i  # 将当前数字加到总和上
    return total_sum  # 返回计算得到的总和
    pass 