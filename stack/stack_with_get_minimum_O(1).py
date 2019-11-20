
def get_minimum(auxilary_stack):
    return auxilary_stack[-1]

def push(s ,auxs, data):
    s.append(data)

    if not auxs:
        auxs.append(data)
    elif data == auxs[-1] or data < auxs[-1]:
        auxs.append(data)
    return s, auxs

def main():
    s = []
    auxs = []
    for i in [2, 6, 4, 1, 5]:
        s, auxs = push(s, auxs, i)
        print(s, auxs)



if __name__ == "__main__":
    main()