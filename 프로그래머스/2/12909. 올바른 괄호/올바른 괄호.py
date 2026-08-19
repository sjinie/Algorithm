def solution(s):
    answer = True
    
    dict_parentheses = {
        "(": True,
        ")": False,
    }
    
    stack_parentheses = []
    
    for item in s:
        if dict_parentheses[item]:
            stack_parentheses.append(item)
        elif not dict_parentheses[item] and not stack_parentheses:
            return False
        else:
            stack_parentheses.pop()
        
    if stack_parentheses:
        return False

    return True