def reshenie( str_input):
    if "(" in str_input:
        ind_end = str_input.find(")")
        ind_start = str_input.rfind("(")
        substr = str_input[(ind_start + 1):ind_end]
        substr2 = '(' + substr + ')'
        substr = vychislenie(substr)
        str_input = str_input.replace(substr2, substr)
        print(str_input)
        reshenie(str_input)
    else:
        str_input = vychislenie(str_input)
        print(str_input)
    return str_input


def vychislenie(substr):
    while "*" in substr:
        ind_umn = substr.find("*")
        num_lf, num_rt = find_left_and_right_nums(substr, ind_umn)
        num = float(num_lf) * float(num_rt)
        substr_in = num_lf + '*' + num_rt
        substr = substr.replace(substr_in, str(num))
        print(substr)
    while "/" in substr:
        ind_umn = substr.find("/")
        num_lf, num_rt = find_left_and_right_nums(substr, ind_umn)
        if num_rt == 0:
            print("error!")
            break;
        num = float(num_lf) / float(num_rt)
        substr_in = num_lf + '/' + num_rt
        substr = substr.replace(substr_in, str(num))
        print(substr)
    while "+" in substr:
        ind_umn = substr.find("+")
        num_lf, num_rt = find_left_and_right_nums(substr, ind_umn)
        num = float(num_lf) + float(num_rt)
        substr_in = num_lf + '+' + num_rt
        substr = substr.replace(substr_in, str(num))
        print(substr)
    while "-" in substr:
        ind_umn = substr.find("-")
        num_lf, num_rt = find_left_and_right_nums(substr, ind_umn)
        num = float(num_lf) - float(num_rt)
        substr_in = num_lf + '-' + num_rt
        substr = substr.replace(substr_in, str(num))
        print(substr)
    return substr


def find_left_and_right_nums(substr, ind_umn):
    num_rt = ''
    if ind_umn == len(substr)-2:
        num_rt = substr[len(substr)-1]
    else:
        for char in range(ind_umn + 1, len(substr)):
            if substr[char].isdigit() or substr[char] =='.':
                num_rt = num_rt + substr[char]
            else:
                break
    num_lf = ''
    if ind_umn == 1:
        num_lf = substr[0]
    else:
        for char in reversed(range(ind_umn)):
            if substr[char].isdigit() or substr[char] =='.':
                num_lf = substr[char] + num_lf
            else:
                break
    return num_lf, num_rt


str_input = input()
str_input = str_input.replace(" ", "")
if '/0'in str_input:
    print('error!')
str_input = str_input.replace("(-", "(0-")
if str_input[0] == "-":
    str_input = "0" + str_input
reshenie(str_input)