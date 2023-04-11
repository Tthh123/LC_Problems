def removeStars(self, s: str) -> str:
    stack = []
    for c in s:
        if (c == "*"):
            stack.pop()
        else:
            stack.append(c)

    retstr = ""
    for a in stack:
        retstr = retstr + a
    return retstr