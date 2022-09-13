expression = input()
operator_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
stack = []
output = []

for char in expression:
    if(char in operator_dict):
        if (len(stack) == 0):
            stack.append(char)
        elif ( ( (stack[-1] in operator_dict) and (operator_dict[char] > operator_dict[stack[-1]]) ) or stack[-1] == "(" ):
            stack.append(char)
        else:
            while ( len(stack) != 0 and ( (stack[-1] in operator_dict) and (operator_dict[char] <= operator_dict[stack[-1]]) ) and stack[-1] != "("):
                output.append(stack.pop())
            stack.append(char)
    elif (char == "("):
        stack.append(char)
    elif (char == ")"):
        while (stack[-1] != "(" and (len(stack) != 0)):
            output.append(stack.pop())
        if (stack[-1] == "("):
            stack.pop()
    else:
        output.append(char)

while (len(stack) != 0):
    output.append(stack.pop())

print(''.join(output))