s = input()
alphabet = [0]*26
word = "sheriff"
amount =0

def count_words():
    global amount
    while True:
        for char in word:
            if alphabet[ord(char)-ord("a")]<=0:
                return
            alphabet[ord(char) - ord("a")] = alphabet[ord(char)-ord("a")]-1
        amount +=1

for char in s:
    order = ord(char)-ord("a")
    alphabet[order] = alphabet[order]+1

count_words()
print(amount)