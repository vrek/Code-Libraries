pairs = {
    "(" : ")",
    "[" : "]",
    "{" : "}"
}

def isValid(sequence: str) -> bool :
    """
    """
    if sequence == "":
        return True
    
    pos = 0
    result = True

    while pos < len(sequence):
        match = pairs.get(sequence[pos])

        if match == None:
            return False
        
        match_index = sequence.find(match)

        if match_index == -1:
            return False
        
        result = result and isValid(sequence[pos+1: match_index])
        pos = match_index + 1

    return result

#def isValid(sequence: str, stack: list) -> bool:
#    sequence = list(sequence)
#    for index, element in enumerate(sequence):
#        if element in ('(', '{','['):
#            stack.append(element)
#            isValid(sequence[1], stack)
#        elif element in (')', '}',']'):
#            if element == ')' and stack[-1] == '(':
#                stack.pop()
#                sequence.pop(index)
#                isValid(sequence, stack)
#            elif element == '{' and stack[-1] == '}':
#                stack.pop()
#                sequence.pop(index)
#                isValid(sequence, stack)
#            elif element == '[' and stack[-1] == ']':
#                stack.pop()
#                sequence.pop(index)
#                isValid(sequence, stack)
#    if len(stack) == 0:
#        return True
#    else:
#        return False
#    
#stack = []
print(isValid("()"))
print(isValid("([]){[}]]"))