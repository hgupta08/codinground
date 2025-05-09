
def areParanthesisBalanced(expr) :
    stack = []

    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:

            # Push the element in the stack
            stack.append(char)
            print(stack)
        else:

            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            print(char)
            print(current_char)
            if current_char == '(':
                print("asd")
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    print(stack)

    # Check Empty Stack
    if stack:
        return False
    return True


# Driver Code
if __name__ == "__main__" :
    expr = "((({}{})))"
    if areParanthesisBalanced(expr) :
        print("Balanced")
    else :
        print("Not Balanced")

# This code is contributed by AnkitRai01 and improved
# by Raju Pitta