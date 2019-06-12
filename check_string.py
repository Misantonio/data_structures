# Function to check parentheses 
def check_string(string): 
    arr_open = ["[","{","("] 
    arr_close = ["]","}",")"] 
    a = [] 
    for char in string: 
        if char in arr_open: 
            a.append(char) 
            print(a)
        elif char in arr_close: 
            pos = arr_close.index(char) 
            if ((len(a) > 0) and (arr_open[pos] == a[-1])): 
                a.pop() 
                print(a)
            else: 
                return "Unbalanced"
    if len(a) == 0: 
        return "Balanced"
    else:
        return "Unbalanced"


if __name__ == "__main__":
    val = "([])"
    print(check_string(val))