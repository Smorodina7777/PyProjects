import re
faces = set()
file = open("Hamlet.txt", "r")
line = "1"
lines = ''
n = 0
word_dict = dict()
len_dict = dict()
chars = set()
list_sentence = []
sentences = []
max_s = 0
while line:
    line = file.readline()
    lines += line
    line =re.sub("[.|,|(|)|:|!|\"|\[|\]|-|\n|—|?|=|1|2|3|4|5|6|7|8|9|0]", " ", line)
    list_line = line.split()
    if len(list_line) != 0:
        if list_line[0].isupper() and list_line[0] not in ["ACT", 'I', 'O', 'A', "T'"]:
            if "/" in list_line[0]:
                ind = list_line[0].find("/")
                faces.add(list_line[0][:ind])
                faces.add(list_line[0][ind+1:])
            else:
                faces.add(list_line[0])
        for word in list_line:
            if word.upper() not in faces:
                word_dict[word.lower()] = word_dict.get(word.lower(), 0) + 1
                len_dict[word.lower()] = len(word)
count_word_list = []
len_word_list = []
for key, value in word_dict.items():
    count_word_list.append((value, key))
for key, value in len_dict.items():
    len_word_list.append((value, key))
count_word_list.sort(reverse=True)
len_word_list.sort(reverse=True)

for name in faces:
    lines = lines.replace(name, "")
sentences = re.split("[.|!|\?|...]", lines)
for s in sentences:
    for ch in s:
        if ch.isalpha():
            chars.add(ch.lower())
    if len(chars)>max_s:
        list_sentence = []
        max_s = len(chars)
        list_sentence.append(s)
        chars =set()
    elif len(chars) == max_s:
        list_sentence.append(s)
        chars = set()
    else:
        chars = set()
file.close()
for name in faces:
    print(name)
print("\n")
print(count_word_list[0][1])
print(len_word_list[0][1])
print(list_sentence[0])