def plusOne(self, digits: List[int]) -> List[int]:
    strno = ""
    for i in digits:
        strno = strno + str(i)
    intno = int(strno)
    intno = intno + 1
    return [int(x) for x in str(intno)]