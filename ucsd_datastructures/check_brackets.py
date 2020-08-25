

def checkBracketMatch(bra1,bra2):
    return (bra1+bra2) in {'()','{}','[]'}


def checkBrackets(s):
    bracket_stack = []
    open_bracket_set = {'(','[','{'}
    closing_bracket_set = {')',']','}'}

    for i,char in enumerate(s,1):
        if char in open_bracket_set:
            bracket_stack.append((char,i))
        if char in closing_bracket_set:
            if len(bracket_stack) == 0 or not checkBracketMatch(bracket_stack.pop()[0],char):
                return i

    return 'Success' if len(bracket_stack)==0 else bracket_stack.pop()[1]


# Tests

num_tests = 55
fnames = ["check_brackets_tests/{:02d}".format(i) for i in range(1,num_tests)]

for fname in fnames:
    f = open(fname)
    test_str = f.read().strip()
    f_ans = open(fname+'.a')
    my_res = checkBrackets(test_str)
    expected_res = f_ans.read().strip()
    assert(str(my_res) == expected_res)
print("Everything looks good!")
