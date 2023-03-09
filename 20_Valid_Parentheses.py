s = "([)]"    #False
# s = "()()()"  #True
# s = "([[((())]])"  #False
# s = "{{{[[[()]]]}}(}" #False
# s = "([](){})" #True
# s = "{[]}"   #True
# s = "[[[]"  # False
print(s)


def brackets_check(string):
    opened_brackets = ["(", "[", "{"]
    closed_brackets = [")", "]", "}"]
    if len(string) % 2 > 0 or s[0] in closed_brackets or string[-1] in opened_brackets:
        return False
    i = 1
    while i < len(string):
        if string[i] in closed_brackets and string[i - 1] != opened_brackets[closed_brackets.index(string[i])]:
            return False

        elif string[i] in closed_brackets and string[i - 1] == opened_brackets[closed_brackets.index(string[i])]:
            string = string[:i - 1] + string[i + 1:]
            i = 0
            continue
        elif i == len(string) - 1 and len(string) > 0:
            return False
        i += 1
    return True


ret = brackets_check(s)
print(ret)
