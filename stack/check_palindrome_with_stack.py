
def check_palindrome(string):
    stack = []
    length = int(len(string)/2)
    even = length %2==0
    for i in range(length):
        stack.append(string[i])
    if even:
        start = length 
    else:
        start = length + 1
    
    for j in range(start, len(string)):
        if string[j] != stack[len(string) -1 - j]:
            print("Not palindrome")
            break 
    
if __name__ == "__main__":
    check_palindrome("aa")