"""
练习: 字典操作

描述：
实现对学生成绩字典的添加、删除、修改和查询操作。

请补全下面的函数，对学生成绩字典进行各种操作。
"""

def student_dict_operations(students_dict, operation, *args):
    """
    对学生字典进行操作
    
    参数:
    - students_dict: 学生字典 {姓名: 成绩}
    - operation: 操作类型 ("add", "remove", "update", "get")
    - args: 操作所需的额外参数
    
    返回:
    - 根据操作返回不同结果
    """
    # 请在下方编写代码
    if operation == "add":
        if len(args) == 2:
            name, score = args
            students_dict[name] = score
        return students_dict
        
    elif operation == "remove":
        if len(args) == 1:
            name = args[0]
            if name in students_dict:
                del students_dict[name]
        return students_dict
        
    elif operation == "update":
        if len(args) == 2:
            name, new_score = args
            if name in students_dict:
                students_dict[name] = new_score
        return students_dict
        
    elif operation == "get":
        if len(args) == 1:
            name = args[0]
            return students_dict.get(name) # 使用 .get() 获取值，不存在时返回 None
        else:
            return None # 参数数量不正确时返回 None
            
    else:
        # 如果操作类型无效，可以选择返回原字典或抛出错误
        print(f"未知的操作类型: {operation}") 
        return students_dict

    pass 