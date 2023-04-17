def isValid(self, s: str) -> bool:
    stack = []
    for p in s:
        if p == "(" or p == "[" or p == "{":
            stack.append(p)
        else:
            if (len(stack) == 0):
                # for edge cases with closing parentheses but no opening parentheses
                return False
            else:
                if (stack[-1] == "(" and p == ")"):
                    stack.pop()
                elif (stack[-1] == "[" and p == "]"):
                    stack.pop()
                elif (stack[-1] == "{" and p == "}"):
                    stack.pop()
                else:
                    #for edge cases with closing parentheses but no opening parentheses
                    return False
    return len(stack) == 0