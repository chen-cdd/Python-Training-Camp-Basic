"""
练习: 列表操作

描述：
实现对学生列表的添加、删除和修改操作。

请补全下面的函数，对学生列表进行各种操作。
"""

def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作
    
    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数
    
    返回:
    - 操作后的学生列表
    """
    # 请在下方编写代码
    if operation == "add":
        if args:  # 确保提供了要添加的学生
            students.append(args[0])
    elif operation == "remove":
        if args and args[0] in students: # 确保提供了要移除的学生且该学生在列表中
            students.remove(args[0])
    elif operation == "update":
        if len(args) == 2: # 确报提供了索引和新值
            index = args[0]
            new_value = args[1]
            if 0 <= index < len(students): # 确保索引有效
                students[index] = new_value
                
    return students # 返回修改后的列表
    pass 