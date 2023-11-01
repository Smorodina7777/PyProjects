def data(str_input):
    list_expression = []
    parameter = ''
    str_input = str_input.replace(" ", "")
    if '/0' in str_input:
        print('error!')
    for char in str_input:
        if char.isalpha():
            parameter = char
    str_input = str_input.replace("(-", "(0-")
    if str_input[0] == "-":
        str_input = "0" + str_input
    decision(str_input, list_expression, parameter)


def decision(str_input, list_expression, parameter):
    if "(" in str_input:
        ind_end = str_input.find(")")
        ind_start = str_input.rfind("(")
        substr = str_input[(ind_start + 1):ind_end]
        substr2 = '(' + substr + ')'
        if parameter in substr:
            list_expression.append(substr)
            str_input = str_input.replace(substr2, parameter)
        else:
            substr = calculation(substr, parameter)
            str_input = str_input.replace(substr2, substr)
        decision(str_input, list_expression, parameter)
    else:
        if parameter in str_input:
            list_expression.append(str_input)
            str_input = str_input.replace(str_input, parameter)
            answer = calculation_x(list_expression, parameter)
            print(answer)
        else:
            str_input = calculation(str_input, parameter)
            print(str_input)
    return str_input, list_expression


def calculation(substr, parameter):
    while "*" in substr:
        ind_sign = substr.find("*")
        num_lf, num_rt = find_left_and_right_nums(substr, ind_sign)
        num = float(num_lf) * float(num_rt)
        substr_in = num_lf + '*' + num_rt
        substr = substr.replace(substr_in, str(num))
    while "/" in substr:
        ind_sign = substr.find("/")
        num_lf, num_rt = find_left_and_right_nums(substr, ind_sign)
        if num_rt == 0:
            print("error!")
            break;
        num = float(num_lf) / float(num_rt)
        substr_in = num_lf + '/' + num_rt
        substr = substr.replace(substr_in, str(num))
    while "+" in substr:
        ind_sign = substr.find("+")
        num_lf, num_rt = find_left_and_right_nums(substr, ind_sign)
        num = float(num_lf) + float(num_rt)
        substr_in = num_lf + '+' + num_rt
        substr = substr.replace(substr_in, str(num))
    while "-" in substr:
        ind_sign = substr.find("-")
        num_lf, num_rt = find_left_and_right_nums(substr, ind_sign)
        num = float(num_lf) - float(num_rt)
        substr_in = num_lf + '-' + num_rt
        substr = substr.replace(substr_in, str(num))
    return substr

def calculation_x(list_expression, parameter):
    answer = 0
    for expression in reversed(list_expression):
        if "*" in expression:
            while "*" in expression:
                ind_sign = expression.find("*")
                num_lf, num_rt = find_left_and_right_nums(expression, ind_sign)
                if num_rt == '':
                    num_rt = parameter
                elif num_lf == '':
                    num_lf = parameter
                if (num_rt.isdigit() or "." in num_rt) and (num_lf.isdigit() or "." in num_lf):
                    num = float(num_lf) * float(num_rt)
                    expression_in = num_lf + '*' + num_rt
                    expression = expression.replace(expression_in, str(num))
                else:
                    expression = expression.replace('*', '?')
        if "/" in expression:
            while "/" in expression:
                ind_sign = expression.find("/")
                num_lf, num_rt = find_left_and_right_nums(expression, ind_sign)
                if num_rt == '':
                    num_rt = parameter
                elif num_lf == '':
                    num_lf = parameter
                if (num_rt.isdigit() or "." in num_rt) and (num_lf.isdigit() or "." in num_lf):
                    if num_rt == 0:
                        print("error!")
                        break;
                    num = float(num_lf) / float(num_rt)
                    expression_in = num_lf + '/' + num_rt
                    expression = expression.replace(expression_in, str(num))
                else:
                    expression = expression.replace('/', '&')
        if "+" in expression:
            while "+" in expression:
                ind_sign = expression.rfind("+")
                num_lf, num_rt = find_left_and_right_nums(expression, ind_sign)
                if num_rt.isdigit() or "." in num_rt:
                    answer -= float(num_rt)
                    expression = expression[:ind_sign] + expression[ind_sign+1:]
                    ind_num = expression.rfind(num_rt)
                    expression = expression[:ind_num] + expression[ind_num+len(num_rt):]
                    if expression == parameter:
                        expression = expression.replace(parameter, '')
                else:
                    expression = expression.replace('+', '#')
            if '#' in expression:
                expression = expression.replace('#', '+')
                ind_sign = expression.rfind("+")
                num_lf, num_rt = find_left_and_right_nums(expression, ind_sign)
                answer -= float(num_lf)
                expression = expression[:ind_sign] + expression[ind_sign + 1:]
                ind_num = expression.rfind(num_lf)
                expression = expression[:ind_num] + expression[ind_num + len(num_lf):]
                if expression == parameter:
                    expression = expression.replace(parameter, '')
        if "-" in expression:
            while "-" in expression:
                ind_sign = expression.rfind("-")
                num_lf, num_rt = find_left_and_right_nums(expression, ind_sign)
                if num_rt.isdigit() or "." in num_rt:
                    answer += float(num_rt)
                    expression = expression[:ind_sign] + expression[ind_sign+1:]
                    ind_num = expression.rfind(num_rt)
                    expression = expression[:ind_num] + expression[ind_num + len(num_rt):]
                    if expression == parameter:
                        expression = expression.replace(parameter, '')
                else:
                    expression = expression.replace('-', '@')
            if '@' in expression:
                expression = expression.replace('@', '-')
                ind_sign = expression.rfind("-")
                num_lf, num_rt = find_left_and_right_nums(expression, ind_sign)
                answer = (answer -float(num_lf))* -1
                expression = expression[:ind_sign] + expression[ind_sign + 1:]
                ind_num = expression.rfind(num_lf)
                expression = expression[:ind_num] + expression[ind_num + len(num_lf):]
                if expression == parameter:
                    expression = expression.replace(parameter, '')
        if '?' in expression:
            expression = expression.replace('?', '*')
            ind_sign = expression.rfind("*")
            num_lf, num_rt = find_left_and_right_nums(expression, ind_sign)
            if num_lf.isdigit():
                answer /= float(num_lf)
                expression = expression[:ind_sign] + expression[ind_sign + 1:]
                ind_num = expression.rfind(num_lf)
                expression = expression[:ind_num] + expression[ind_num + len(num_lf):]
            elif num_rt.isdigit():
                answer /= float(num_rt)
                expression = expression[:ind_sign] + expression[ind_sign + 1:]
                ind_num = expression.rfind(num_rt)
                expression = expression[:ind_num] + expression[ind_num + len(num_rt):]
            if expression == parameter:
                expression = expression.replace(parameter, '')
        if '&' in expression:
            expression = expression.replace('&', '/')
            ind_sign = expression.rfind("/")
            num_lf, num_rt = find_left_and_right_nums(expression, ind_sign)
            if num_lf.isdigit():
                answer = float(num_lf) /answer
                expression = expression[:ind_sign] + expression[ind_sign + 1:]
                ind_num = expression.rfind(num_lf)
                expression = expression[:ind_num] + expression[ind_num + len(num_lf):]
            elif num_rt.isdigit():
                answer *= float(num_rt)
                expression = expression[:ind_sign] + expression[ind_sign + 1:]
                ind_num = expression.rfind(num_rt)
                expression = expression[:ind_num] + expression[ind_num + len(num_rt):]
            if expression == parameter:
                expression = expression.replace(parameter, '')
    return answer


def find_left_and_right_nums(substr, ind_sign):
    num_rt = ''
    if ind_sign == len(substr)-2:
        num_rt = substr[len(substr)-1]
    else:
        for char in range(ind_sign + 1, len(substr)):
            if substr[char].isdigit() or substr[char] =='.':
                num_rt = num_rt + substr[char]
            else:
                break
    num_lf = ''
    if ind_sign == 0:
        num_lf = 0
    elif ind_sign == 1:
        num_lf = substr[0]
    else:
        for char in reversed(range(ind_sign)):
            if substr[char].isdigit() or substr[char] =='.':
                num_lf = substr[char] + num_lf
            else:
                break
    return num_lf, num_rt


str_input = input()
data(str_input)