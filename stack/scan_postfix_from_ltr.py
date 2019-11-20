
def operation(a, b, operator):

    if operator == "*":
        return a*b
    elif operator == "-":
        k = a-b
        return  -(k) if k < 0 else k
    elif operator == "+":
        return a+b
    elif operator == "/":
        return a/b

def is_opertor(operator):
    return operator in "*-/+"

def main():
    expression = "123*+5-"
    stack = []
    for i in expression:
        # if not operator then push into stack
        if (is_opertor(i)):
            # pop two values from stack and perform operation and push back into stack
            item1 = stack.pop(-1)
            item2 = stack.pop(-1)
            # print("items=>", item1, item2)
            item = operation(item1, item2, i)
            stack.append(int(item))
            # print(stack)
        else:
            # print(stack)
            stack.append(int(i))

    if len(stack) > 0:
        print(stack)
        # print("Something went wrong")
    else:
        print("Everything is alright")
if __name__ == "__main__":
    main()