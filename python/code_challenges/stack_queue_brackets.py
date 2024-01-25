from data_structures.queue import Queue

# Used ChatGPT to help outline this code
def multi_bracket_validation(string):
    stack = []

    for character in string:
        if character == "(" or character == "[" or character == "{":
            stack.append(character)
        elif character == ")" or character == "]" or character == "}":
            if len(stack) == 0:
                return False
            
            top_of_stack = stack.pop()

            if not compare(top_of_stack, character):
                return False
        
    if len(stack) != 0:
        return False
    
    return True
    

def compare(opening, closing):
    if opening == '(' and closing == ')':
        return True
    if opening == '[' and closing == ']':
        return True
    if opening == '{' and closing == '}':
        return True
    return False
