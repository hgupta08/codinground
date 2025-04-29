def isbalancedparanthesis(expr):

    s=[]

    for char in expr:
        if char in ["{","[","("]:
            s.append(char)
        else:
           if not s:
               return False
           current_char=s.pop()

           if current_char=='(':
                if char !=")":
                    return False

           if current_char=='{':
                if char !="}":
                    return False
           if current_char=='[':
                if char !="]":
                    return False

    if s:
        return False
    return True





expr=""
print(isbalancedparanthesis(expr))